# inventory_manager.py
from product import Product
from supplier import Supplier
from purchase_order import PurchaseOrder

class InventoryManager:
    def __init__(self):
        self.products = {}
        self.suppliers = {}
        self.purchase_orders = {}

    def manage_products(self, action, product=None):
        if action == "add" and product:
            self.products[product.id] = product
        elif action == "update" and product:
            self.products[product.id] = product
        elif action == "delete" and product:
            self.products.pop(product.id, None)
        elif action == "get":
            return list(self.products.values())

    def manage_suppliers(self, action, supplier=None):
        if action == "add" and supplier:
            self.suppliers[supplier.id] = supplier
        elif action == "update" and supplier:
            self.suppliers[supplier.id] = supplier
        elif action == "delete" and supplier:
            self.suppliers.pop(supplier.id, None)
        elif action == "get":
            return list(self.suppliers.values())

    def manage_purchase_orders(self, action, order=None):
        if action == "add" and order:
            self.purchase_orders[order.order_id] = order
        elif action == "update" and order:
            self.purchase_orders[order.order_id] = order
        elif action == "delete" and order:
            self.purchase_orders.pop(order.order_id, None)
        elif action == "get":
            return list(self.purchase_orders.values())

    def generate_reports(self):
        return {
            "products": [p.summary() for p in self.products.values()],
            "suppliers": [s.summary() for s in self.suppliers.values()],
            "purchase_orders": [po.summary() for po in self.purchase_orders.values()]
        }
