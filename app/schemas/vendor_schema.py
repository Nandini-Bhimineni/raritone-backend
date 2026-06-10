from pydantic import BaseModel
from datetime import datetime


class VendorCreate(BaseModel):
    vendor_name: str
    email: str
    phone: str
    address: str
    vendor_status: str = "Pending"
    created_at: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    updated_at: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")



class VendorUpdate(BaseModel):
    vendor_name: str | None = None
    phone: str | None = None
    address: str | None = None


class KYCUpdate(BaseModel):
    gst_number: str
    kyc_document: str


class VendorResponse(BaseModel):
    id: int
    vendor_name: str
    email: str
    vendor_status: str
    is_verified: bool
    created_at: str
    updated_at: str

    class Config:
        from_attributes = True