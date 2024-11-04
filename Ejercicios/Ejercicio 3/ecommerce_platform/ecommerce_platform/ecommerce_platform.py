from product import Product
from user import User
from order import Order

class EcommercePlatform:
    def __init__(self):
        self.products = {}
        self.users = {}
        self.orders = {}
        self.order_id_counter = 1

    def manage_products(self, action, product=None):
        if action == "add" and product:
            self.products[product.id] = product
        elif action == "delete" and product:
            self.products.pop(product.id, None)

    def manage_users(self, action, user=None):
        if action == "add" and user:
            self.users[user.user_id] = user

    def create_order(self, user_id):
        user = self.users.get(user_id)
        if not user:
            raise ValueError("Usuario no encontrado.")
        total = user.checkout(self.products)
        order = Order(self.order_id_counter, user, user.cart.copy(), total)
        self.orders[self.order_id_counter] = order
        self.order_id_counter += 1
        return order

    def generate_reports(self):
        sales = sum(order.total_amount for order in self.orders.values() if order.status == "completed")
        return {
            "total_sales": sales,
            "total_orders": len(self.orders)
        }
