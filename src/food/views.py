from typing import Annotated

from fastapi import APIRouter, Depends
from src.food.schemas import FoodSchema
from src.food.dependencies import create_food_depend


router = APIRouter(prefix="/food", tags=["food"])


@router.post(
    "/",
    tags=["food"],
    summary="Create a new food",
    response_model=FoodSchema,
    response_model_exclude_none=True,
)
async def create_food(food: Annotated[FoodSchema, Depends(create_food_depend)]):
    return food
