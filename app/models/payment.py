class Payment:
    def __init__(
        self,
        payment_id,
        customer_id,
        amount,
        payment_type,
        status
    ):
        self.payment_id = payment_id
        self.customer_id = customer_id
        self.amount = amount
        self.payment_type = payment_type
        self.status = status

