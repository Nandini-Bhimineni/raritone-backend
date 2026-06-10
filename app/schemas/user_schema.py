from pydantic import BaseModel, EmailStr, Field
from datetime import datetime


class UserSignup(BaseModel):
    full_name: str = Field(
        ...,
        min_length=3,
        max_length=100
    )

    email: EmailStr

    password: str = Field(
        ...,
        min_length=6
    )


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class OTPVerification(BaseModel):
    email: EmailStr
    otp: str


class PasswordReset(BaseModel):
    email: EmailStr

    new_password: str = Field(
        ...,
        min_length=6
    )


class UserResponse(BaseModel):
    id: int

    full_name: str

    email: str

    role: str

    is_verified: bool

    is_active: bool

    created_at: datetime | None = None

    updated_at: datetime | None = None

    class Config:
        from_attributes = True