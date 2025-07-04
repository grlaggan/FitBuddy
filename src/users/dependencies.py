from jwt import InvalidTokenError, ExpiredSignatureError
from typing import Annotated
from sqlalchemy.ext.asyncio.session import AsyncSession
from fastapi import Depends, HTTPException, status, Body
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from src.database import UserModel
from src.users.password import verify_password
from src.users.jwt import encode, decode
from src.users.crud import create_user, get_user_by_id, get_user_by_username
from src.users.schemas import CreateUserSchema, TokensSchema, UserSchema
from src.database.init import init_db
from src import sets

Session = Annotated[AsyncSession, Depends(init_db.async_session)]
http_bearer = HTTPBearer()


async def create_user_depend(user: CreateUserSchema, session: Session) -> UserModel:
    if user.password != user.password_second:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Passwords are not the same!",
        )

    user_obj = await get_user_by_id(user.id, session)

    if user_obj:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists!",
        )

    return await create_user(user, session)


async def login_depend(
    username: Annotated[str, Body()], password: Annotated[str, Body()], session: Session
) -> TokensSchema:
    user = await get_user_by_username(username, session)
    user = UserSchema.model_validate(user)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found!",
        )

    if not verify_password(password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect password!",
        )

    access_token = encode({"sub": user.id})
    refresh_token = encode(
        {"sub": user.id}, refresh_token_days_expire=sets.jwt.refresh_token_days_expire
    )

    return TokensSchema(
        user_id=user.id,
        access_token=access_token,
        refresh_token=refresh_token,
    )


async def refresh_depend(refresh_token: Annotated[str, Body()]) -> TokensSchema:
    try:
        payload = decode(refresh_token)

        access_token = encode({"sub": payload["sub"]})
        refresh_token = encode({"sub": payload["sub"]})

        return TokensSchema(
            user_id=int(payload["sub"]),
            access_token=access_token,
            refresh_token=refresh_token,
        )
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired!",
        )
    except InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect token!",
        )


async def check_auth_depend(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(http_bearer)],
):
    try:
        decode(credentials.credentials)
        return {"detail": "Authorization successful!"}
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired!",
        )
