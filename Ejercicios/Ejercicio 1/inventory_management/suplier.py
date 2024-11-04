# supplier.py
class Supplier:
    def __init__(self, supplier_id, name, contact_info):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("El nombre debe ser una cadena no vacía.")
        if not isinstance(contact_info, str) or not contact_info.strip():
            raise ValueError("La información de contacto debe ser una cadena no vacía.")
        
        self.id = supplier_id
        self.name = name
        self.contact_info = contact_info
        self.products_supplied = set()

    def add_product(self, product_id):
        self.products_supplied.add(product_id)

    def remove_product(self, product_id):
        self.products_supplied.discard(product_id)

    def summary(self):
        return {
            "id": self.id,
            "name": self.name,
            "contact_info": self.contact_info,
            "products_supplied": list(self.products_supplied)
        }
