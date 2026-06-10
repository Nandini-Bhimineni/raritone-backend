from pydantic import BaseModel


class WalletCreate(BaseModel):
    customer_id: int
    balance: float


class TransactionCreate(BaseModel):
    customer_id: int
    amount: float
    transaction_type: str


class SettlementCreate(BaseModel):
    vendor_id: int
    amount: float


class PayoutRequestCreate(BaseModel):
    vendor_id: int
    amount: float


class PaymentResponse(BaseModel):
    id: int
    status: str
