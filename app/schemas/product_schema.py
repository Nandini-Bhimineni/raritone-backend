from pydantic import BaseModel
from typing import Optional


class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    stock: int
    category_id: int

    variant: Optional[str] = None
    image_url: Optional[str] = None

    brand: Optional[str] = None
    sku: Optional[str] = None

    status: str = "Active"


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None
    category_id: Optional[int] = None

    variant: Optional[str] = None
    image_url: Optional[str] = None

    brand: Optional[str] = None
    sku: Optional[str] = None

    status: Optional[str] = None


class ProductResponse(BaseModel):
    id: int
    name: str
    price: float

    class Config:
        from_attributes = True