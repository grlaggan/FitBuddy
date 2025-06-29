from typing import Annotated

from pydantic import BaseModel
from pydantic.config import ConfigDict
from pydantic.functional_validators import AfterValidator

from src.users.password import validate_password


class BaseUserSchema(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        strict=True,
        from_attributes=True,
    )

    username: str
    password: str = Annotated[str, AfterValidator(validate_password)]
    first_name: str | None
    last_name: str | None


class UserSchema(BaseUserSchema):
    id: int
    password: bytes


class CreateUserSchema(BaseUserSchema):
    id: int
    password_second: str = Annotated[str, AfterValidator(validate_password)]


class TokensSchema(BaseModel):
    user_id: int
    access_token: str
    refresh_token: str
