from pydantic import BaseModel, Field
from typing import Literal, Optional

# --- WALLET SCHEMAS ---
class WalletCreate(BaseModel):
    customer_id: int
    initial_balance: float = Field(default=0.0, ge=0.0)

class WalletAmountUpdate(BaseModel):
    customer_id: int
    amount: float = Field(..., gt=0.0)

# --- TRANSACTION SCHEMAS ---
class TransactionCreate(BaseModel):
    customer_id: Optional[int] = None
    vendor_id: Optional[int] = None
    amount: float = Field(..., gt=0.0)
    payment_method: Literal["Wallet", "UPI", "Credit Card", "Debit Card", "Net Banking", "Cash On Delivery"]
    status: Literal["Pending", "Success", "Failed"] = "Pending"
    reference_number: Optional[str] = None
    remarks: Optional[str] = None

# --- SETTLEMENT SCHEMAS ---
class SettlementCreate(BaseModel):
    vendor_id: int
    amount: float = Field(..., gt=0.0)
    remarks: Optional[str] = None

# --- PAYOUT SCHEMAS ---
class PayoutCreate(BaseModel):
    vendor_id: int
    amount: float = Field(..., gt=0.0)
    remarks: Optional[str] = None

# --- REFUND SCHEMAS ---
class RefundCreate(BaseModel):
    transaction_id: str
    amount: float = Field(..., gt=0.0)
    remarks: Optional[str] = None