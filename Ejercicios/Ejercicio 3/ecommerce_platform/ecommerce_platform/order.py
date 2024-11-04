class Order:
    def __init__(self, order_id, user, order_items, total_amount):
        self.order_id = order_id
        self.user = user
        self.order_items = order_items
        self.total_amount = total_amount
        self.status = 'pending'

    def process_payment(self, payment_info):
        if payment_info.get("status") == "success":
            self.status = 'completed'
        else:
            raise ValueError("Pago fallido.")

    def update_status(self, new_status):
        self.status = new_status

    def summary(self):
        return {
            "order_id": self.order_id,
            "user_id": self.user.user_id,
            "total_amount": self.total_amount,
            "status": self.status
        }
