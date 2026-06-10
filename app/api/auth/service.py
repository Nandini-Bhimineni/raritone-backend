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
        "role": "customer",
        "is_verified": False,
        "is_active": True,
        "otp": otp,
        "created_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "updated_at": datetime.now().strftime(
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
            if not user.get("is_verified",False):
                return{
                    "error":"Please verify OTP first"
                }

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
            user["updated_at"]=datetime.now().strftime(
                "%Y=%m-%d %H:%M:%S"
            )

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
            user["updated_at"]=datetime.now().strftime(
                "%Y=%m-%d %H:%M:%S"
            )

            return {
                "message": "Password reset successful"
            }

    return {
        "error": "User not found"
    }


def get_all_users():

    safe_users = []

    for user in users:

        safe_users.append(
            {
                "id": user["id"],
                "full_name": user["full_name"],
                "email": user["email"],
                "role": user.get("role", "customer"),
                "is_verified": user["is_verified"],
                "is_active": user.get("is_active", True),
                "created_at": user.get("created_at"),
                "updated_at": user.get("updated_at")
            }
        )

    return safe_users


def resend_otp(email):

    for user in users:

        if user["email"] == email:

            otp = str(
                random.randint(
                    100000,
                    999999
                )
            )

            user["otp"] = otp

            user["updated_at"] = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            return {
                "message": "OTP resent successfully",
                "otp": otp
            }

    return {
        "error": "User not found"
    }


def get_user(email):

    for user in users:

        if user["email"] == email:

            return {
                "id": user["id"],
                "full_name": user["full_name"],
                "email": user["email"],
                "role": user.get("role", "customer"),
                "is_verified": user["is_verified"],
                "is_active": user.get("is_active", True),
                "created_at": user.get("created_at"),
                "updated_at": user.get("updated_at")
            }

    return {
        "error": "User not found"
    }


def get_user_count():

    return {
        "total_users": len(users)
    }