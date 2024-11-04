class Product:
    def __init__(self, product_id, name, description, price, stock):
        if price <= 0 or stock < 0:
            raise ValueError("El precio y el stock deben ser positivos.")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("El nombre debe ser una cadena no vacía.")
        if not isinstance(description, str) or not description.strip():
            raise ValueError("La descripción debe ser una cadena no vacía.")
        
        self.id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock

    def update_stock(self, new_stock):
        if new_stock < 0:
            raise ValueError("El stock debe ser un valor positivo.")
        self.stock = new_stock

    def apply_discount(self, discount_percentage):
        if not (0 <= discount_percentage <= 100):
            raise ValueError("El porcentaje de descuento debe estar entre 0 y 100.")
        self.price *= (1 - discount_percentage / 100)

    def summary(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "stock": self.stock
        }
