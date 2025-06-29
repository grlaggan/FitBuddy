import bcrypt
from src.users.exceptions import InvalidPassword


def hash_password(password: str) -> bytes:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def verify_password(password: str, hashed_password: bytes):
    return bcrypt.checkpw(password.encode(), hashed_password)


def validate_password(value: str):
    if len(value) < 8:
        raise InvalidPassword("Password must be at least 8 characters long")

    has_digits = any(char.isdigit() for char in value)
    has_upper = any(char.isupper() for char in value)
    has_lower = any(char.islower() for char in value)

    if not has_digits or not has_upper or not has_lower:
        raise InvalidPassword(
            "Password must contain at least one digit, one upper, one lower"
        )

    return True
