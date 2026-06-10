from pydantic import BaseModel
from typing import Optional, Literal

ShippingStatusType = Literal["Pending", "Packed", "Dispatched", "In-Transit", "Out For Delivery", "Delivered", "Cancelled"]

class ShippingCreate(BaseModel):
    order_id: int
    customer_id: int
    vendor_id: int
    courier: str
    shipping_address: str
    estimated_delivery: str
    delivery_notes: Optional[str] = None

class ShippingResponse(BaseModel):
    shipment_id: str
    order_id: int
    customer_id: int
    vendor_id: int
    courier: str
    tracking_number: str
    shipping_address: str
    status: ShippingStatusType
    estimated_delivery: str
    actual_delivery_date: Optional[str] = None
    delivery_notes: Optional[str] = None
    created_at: str
    updated_at: str