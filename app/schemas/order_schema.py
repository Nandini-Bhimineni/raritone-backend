from pydantic import BaseModel

class OrderCreate(BaseModel):
    customer_id: int
    product_id: int
    quantity: int
    total_price: float
    status: str = "Pending"