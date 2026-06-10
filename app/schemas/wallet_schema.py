from pydantic import BaseModel
from typing import Optional


class WalletCreate(BaseModel):
    customer_id: str
    balance: float


class WalletUpdate(BaseModel):
    balance: Optional[float] = None


class WalletResponse(BaseModel):
    _id: Optional[str] = None
    customer_id: str
    balance: float

    class Config:
        from_attributes = True
