# purchase_order.py
class PurchaseOrder:
    VALID_STATUSES = {'pendiente', 'completada', 'cancelada'}

    def __init__(self, order_id, supplier):
        if supplier is None:
            raise ValueError("El proveedor debe existir.")
        
        self.order_id = order_id
        self.supplier = supplier
        self.order_items = []
        self.status = 'pendiente'

    def create_order(self, items):
        for item in items:
            if item["quantity"] <= 0:
                raise ValueError("La cantidad de los artículos debe ser positiva.")
            self.order_items.append(item)

    def update_status(self, new_status):
        if new_status not in self.VALID_STATUSES:
            raise ValueError("Estado inválido.")
        self.status = new_status

    def summary(self):
        return {
            "order_id": self.order_id,
            "supplier": self.supplier.summary(),
            "order_items": self.order_items,
            "status": self.status
        }
