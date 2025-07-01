from sqlalchemy.ext.asyncio.session import AsyncSession
from datetime import datetime, timezone

from src.food.models import FoodModel
from src.food.schemas import CreateFoodWithUserIdSchema


async def create_food(
    session: AsyncSession, food: CreateFoodWithUserIdSchema
) -> FoodModel:
    now = datetime.now(tz=timezone.utc)
    str_now = now.strftime("%Y-%m-%d")

    food_obj = FoodModel(
        **food.model_dump(),
        date=str_now,
    )

    session.add(food_obj)
    await session.commit()
    await session.refresh(food_obj)

    return food_obj
