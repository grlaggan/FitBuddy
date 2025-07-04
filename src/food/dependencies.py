from typing import Annotated
from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio.session import AsyncSession

from src.food.crud import create_food
from src.database.init import init_db
from src.food.schemas import CreateFoodSchema, CreateFoodWithUserIdSchema, FoodSchema
from src.users.jwt import decode

http_bearer = HTTPBearer()
Session = Annotated[AsyncSession, Depends(init_db.async_session)]


async def create_food_depend(
    food_data: CreateFoodSchema,
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(http_bearer)],
    session: Session,
):
    payload = decode(credentials.credentials)

    food_with_user_id = CreateFoodWithUserIdSchema(
        **food_data.model_dump(), user_id=int(payload["sub"])
    )
    food = await create_food(
        food=food_with_user_id,
        session=session,
    )

    return FoodSchema.model_validate(food)
