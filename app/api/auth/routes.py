from fastapi import APIRouter

from app.schemas.user_schema import (
    UserSignup,
    UserLogin,
    OTPVerification,
    PasswordReset
)

from app.api.auth.service import (
    create_user,
    login_user,
    verify_otp,
    reset_password,
    get_all_users
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/signup")
def signup(user: UserSignup):
    return create_user(user)


@router.post("/login")
def login(user: UserLogin):
    return login_user(user)


@router.post("/verify-otp")
def verify(user: OTPVerification):
    return verify_otp(user)


@router.post("/reset-password")
def reset(user: PasswordReset):
    return reset_password(user)


@router.get("/users")
def users():
    return get_all_users()