class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, product_id, quantity):
        if quantity <= 0:
            raise ValueError("La cantidad debe ser positiva.")
        self.items[product_id] = self.items.get(product_id, 0) + quantity

    def remove_item(self, product_id, quantity):
        if product_id not in self.items or quantity > self.items[product_id]:
            raise ValueError("Cantidad no válida o producto no encontrado en el carrito.")
        self.items[product_id] -= quantity
        if self.items[product_id] <= 0:
            del self.items[product_id]

    def calculate_total(self, product_catalog):
        return sum(product_catalog[product_id].price * quantity for product_id, quantity in self.items.items())

    def clear_cart(self):
        self.items.clear()
