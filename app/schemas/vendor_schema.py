from pydantic import BaseModel


class VendorCreate(BaseModel):
    vendor_name: str
    email: str
    phone: str
    address: str


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

    class Config:
        from_attributes = True