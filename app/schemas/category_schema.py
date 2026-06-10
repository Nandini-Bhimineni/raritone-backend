from pydantic import BaseModel
from typing import Optional


class CategoryCreate(BaseModel):
    name: str
    description: str

    image_url: Optional[str] = None

    status: str = "Active"


class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

    image_url: Optional[str] = None

    status: Optional[str] = None


class CategoryResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True