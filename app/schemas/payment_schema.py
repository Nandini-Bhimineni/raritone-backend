from pydantic import BaseModel, Field
from datetime import datetime

class WalletCreate(BaseModel):
    customer_id: int
    initial_balance: float = Field(default=0.0, ge=0.0)

class WalletAmountUpdate(BaseModel):
    customer_id: int
    amount: float = Field(..., gt=0.0, description="Amount must be greater than zero")

class WalletResponse(BaseModel):
    id: int
    customer_id: int
    balance: float
    created_at: str
    updated_at: str

    class Config:
        from_attributes = True