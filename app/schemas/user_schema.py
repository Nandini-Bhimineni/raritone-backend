from pydantic import BaseModel, EmailStr, Field


class UserSignup(BaseModel):
    full_name: str = Field(..., min_length=3, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=6)


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class OTPVerification(BaseModel):
    email: EmailStr
    otp: str


class PasswordReset(BaseModel):
    email: EmailStr
    new_password: str = Field(..., min_length=6)


class UserResponse(BaseModel):
    id: int
    full_name: str
    email: str
    is_verified: bool

    class Config:
        from_attributes = True