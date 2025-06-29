from fastapi import APIRouter, Depends
from typing import Annotated

from src.users import schemas, models, dependencies

router = APIRouter(prefix="/users", tags=["users"])


@router.post(
    "/register",
    response_model=schemas.UserSchema,
    summary="Register new user",
)
async def register(
    user: Annotated[models.UserModel, Depends(dependencies.create_user_depend)],
):
    return user


@router.get("/login", response_model=schemas.TokensSchema, summary="Login user")
async def login(
    user_tokens: Annotated[schemas.TokensSchema, Depends(dependencies.login_depend)],
):
    return user_tokens
