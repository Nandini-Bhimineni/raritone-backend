from sqlalchemy import Column, Integer, String, Boolean
from app.database.base import Base


class Vendor(Base):
    __tablename__ = "vendors"

    id = Column(Integer, primary_key=True, index=True)
    vendor_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String)
    address = Column(String)
    gst_number = Column(String)
    kyc_document = Column(String)
    is_verified = Column(Boolean, default=False)