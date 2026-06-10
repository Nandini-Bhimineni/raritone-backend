class Inventory:
    def __init__(
        self,
        inventory_id,
        product_id,
        product_name,
        quantity,
        price
    ):
        self.inventory_id = inventory_id
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity
        self.price = price