from pydantic import BaseModel

class InventoryCreate(BaseModel):
    product_id: int
    product_name: str
    quantity: int
    price: float

class InventoryResponse(InventoryCreate):
    inventory_id: int