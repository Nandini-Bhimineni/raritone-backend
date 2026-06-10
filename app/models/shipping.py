class Shipping:
    def __init__(
        self,
        shipment_id,
        order_id,
        customer_id,
        vendor_id,
        courier,
        tracking_number,
        shipping_address,
        status,
        estimated_delivery,
        actual_delivery_date,
        delivery_notes,
        created_at,
        updated_at
    ):
        self.shipment_id = shipment_id
        self.order_id = order_id
        self.customer_id = customer_id
        self.vendor_id = vendor_id
        self.courier = courier
        self.tracking_number = tracking_number
        self.shipping_address = shipping_address
        self.status = status
        self.estimated_delivery = estimated_delivery
        self.actual_delivery_date = actual_delivery_date
        self.delivery_notes = delivery_notes
        self.created_at = created_at
        self.updated_at = updated_at