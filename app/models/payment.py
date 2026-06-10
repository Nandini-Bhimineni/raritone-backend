from sqlalchemy import Column, Integer, Float, String
from app.database.base import Base

class Wallet(Base):
    __tablename__ = "wallets"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, unique=True, nullable=False)
    balance = Column(Float, default=0.0)
    created_at = Column(String)
    updated_at = Column(String)