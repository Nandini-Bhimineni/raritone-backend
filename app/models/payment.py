from sqlalchemy import Column, Integer, Float, String, Enum
from app.database.base import Base

class Wallet(Base):
    __tablename__ = "wallets"
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, unique=True, nullable=False)
    balance = Column(Float, default=0.0)
    created_at = Column(String)
    updated_at = Column(String)

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    transaction_id = Column(String, unique=True, index=True)
    customer_id = Column(Integer, nullable=True)
    vendor_id = Column(Integer, nullable=True)
    amount = Column(Float, nullable=False)
    payment_method = Column(String, nullable=False)  # Wallet, UPI, Credit Card, etc.
    status = Column(String, default="Pending")       # Pending, Success, Failed
    reference_number = Column(String, nullable=True)
    remarks = Column(String, nullable=True)
    created_at = Column(String)
    updated_at = Column(String)

class Settlement(Base):
    __tablename__ = "settlements"
    id = Column(Integer, primary_key=True, index=True)
    settlement_id = Column(String, unique=True, index=True)
    vendor_id = Column(Integer, nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(String, default="Pending")
    remarks = Column(String, nullable=True)
    created_at = Column(String)
    updated_at = Column(String)

class Payout(Base):
    __tablename__ = "payouts"
    id = Column(Integer, primary_key=True, index=True)
    payout_id = Column(String, unique=True, index=True)
    vendor_id = Column(Integer, nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(String, default="Pending") # Pending, Approved, Rejected
    remarks = Column(String, nullable=True)
    created_at = Column(String)
    updated_at = Column(String)

class Refund(Base):
    __tablename__ = "refunds"
    id = Column(Integer, primary_key=True, index=True)
    refund_id = Column(String, unique=True, index=True)
    transaction_id = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(String, default="Pending")
    remarks = Column(String, nullable=True)
    created_at = Column(String)
    updated_at = Column(String)