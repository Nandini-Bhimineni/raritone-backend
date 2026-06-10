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
    resend_otp,
    reset_password,
    get_user,
    get_user_count,
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


@router.post("/resend-otp")
def resend(email: str):
    return resend_otp(email)


@router.post("/reset-password")
def reset(user: PasswordReset):
    return reset_password(user)


@router.get("/me")
def me(email: str):
    return get_user(email)


@router.get("/count")
def count():
    return get_user_count()


@router.get("/users")
def users():
    return get_all_users()