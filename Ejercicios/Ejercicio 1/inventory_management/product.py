# product.py
class Product:
    def __init__(self, product_id, name, description, price, quantity_in_stock):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("El nombre debe ser una cadena no vacía.")
        if not isinstance(description, str) or not description.strip():
            raise ValueError("La descripción debe ser una cadena no vacía.")
        if price <= 0:
            raise ValueError("El precio debe ser un valor positivo.")
        if quantity_in_stock < 0:
            raise ValueError("La cantidad en stock debe ser positiva.")

        self.id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def update_price(self, new_price):
        if new_price <= 0:
            raise ValueError("El nuevo precio debe ser un valor positivo.")
        self.price = new_price

    def update_quantity(self, new_quantity):
        if new_quantity < 0:
            raise ValueError("La nueva cantidad debe ser positiva.")
        self.quantity_in_stock = new_quantity

    def summary(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "quantity_in_stock": self.quantity_in_stock
        }
