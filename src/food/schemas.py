from pydantic import BaseModel
from pydantic.config import ConfigDict


class BaseFoodSchema(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        from_attributes=True,
    )

    calories: int
    protein: int
    carbohydrates: int
    fats: int


class CreateFoodSchema(BaseFoodSchema):
    pass


class CreateFoodWithUserIdSchema(CreateFoodSchema):
    user_id: int


class FoodSchema(BaseFoodSchema):
    id: int
    user_id: int
    date: str
