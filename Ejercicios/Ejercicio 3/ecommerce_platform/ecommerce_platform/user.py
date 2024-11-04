class User:
    def __init__(self, user_id, username, email, password):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.cart = {}

    def add_to_cart(self, product_id, quantity):
        if quantity <= 0:
            raise ValueError("La cantidad debe ser positiva.")
        if product_id in self.cart:
            self.cart[product_id] += quantity
        else:
            self.cart[product_id] = quantity

    def remove_from_cart(self, product_id, quantity):
        if product_id not in self.cart:
            raise ValueError("Producto no encontrado en el carrito.")
        if quantity > self.cart[product_id]:
            raise ValueError("No se puede remover más de la cantidad existente en el carrito.")
        self.cart[product_id] -= quantity
        if self.cart[product_id] == 0:
            del self.cart[product_id]

    def checkout(self, product_catalog):
        total = 0
        for product_id, quantity in self.cart.items():
            product = product_catalog.get(product_id)
            if not product or product.stock < quantity:
                raise ValueError(f"Producto '{product_id}' no disponible en la cantidad solicitada.")
            total += product.price * quantity
        self.cart.clear()
        return total
