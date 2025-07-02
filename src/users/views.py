from fastapi import APIRouter, Depends
from typing import Annotated

from src.users import schemas, models, dependencies
from src.users.schemas import TokensSchema

router = APIRouter(prefix="/users", tags=["users"])


@router.post(
    "/register",
    response_model=schemas.UserSchema,
    summary="Register new user",
    response_model_exclude_none=True,
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


@router.post("/refresh", response_model=schemas.TokensSchema, summary="Refresh user")
async def refresh(
    user_tokens: Annotated[schemas.TokensSchema, Depends(dependencies.refresh_depend)],
):
    return user_tokens


@router.get("/check_auth", summary="Check if user is authenticated")
async def check_auth(result: Annotated[dict, Depends(dependencies.check_auth_depend)]):
    return result
