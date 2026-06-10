from pydantic import BaseModel


class CustomerCreate(BaseModel):
    name: str
    email: str
    phone: str
    address: str


class CustomerUpdate(BaseModel):
    name: str | None = None
    phone: str | None = None
    address: str | None = None


class CustomerResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True