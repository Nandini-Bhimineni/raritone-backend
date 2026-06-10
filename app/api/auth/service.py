from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
import random

users = []

SECRET_KEY = "RARITONE_SECRET_KEY"
ALGORITHM = "HS256"

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password):
    return pwd_context.hash(password)


def verify_password(
    plain_password,
    hashed_password
):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )


def create_access_token(data):

    payload = data.copy()

    payload["exp"] = (
        datetime.utcnow()
        + timedelta(hours=1)
    )

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


def create_user(user):

    for existing_user in users:

        if existing_user["email"] == user.email:
            return {
                "error": "Email already registered"
            }

    otp = str(
        random.randint(
            100000,
            999999
        )
    )

    new_user = {
        "id": len(users) + 1,
        "full_name": user.full_name,
        "email": user.email,
        "password": hash_password(
            user.password
        ),
        "is_verified": False,
        "otp": otp,
        "created_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    }

    users.append(new_user)

    return {
        "message": "User registered successfully",
        "otp": otp,
        "user": {
            "id": new_user["id"],
            "full_name": new_user["full_name"],
            "email": new_user["email"]
        }
    }


def login_user(data):

    for user in users:

        if user["email"] == data.email:

            if not verify_password(
                data.password,
                user["password"]
            ):
                return {
                    "error": "Invalid password"
                }

            token = create_access_token(
                {
                    "sub": user["email"]
                }
            )

            return {
                "access_token": token,
                "token_type": "bearer"
            }

    return {
        "error": "User not found"
    }


def verify_otp(data):

    for user in users:

        if user["email"] == data.email:

            if user["otp"] != data.otp:
                return {
                    "error": "Invalid OTP"
                }

            user["is_verified"] = True

            return {
                "message": "OTP verified successfully"
            }

    return {
        "error": "User not found"
    }


def reset_password(data):

    for user in users:

        if user["email"] == data.email:

            user["password"] = hash_password(
                data.new_password
            )

            return {
                "message": "Password reset successful"
            }

    return {
        "error": "User not found"
    }


def get_all_users():
    return users