from pydantic import BaseModel
from pydantic.config import ConfigDict
from src.core import TrainStatus


class BaseTrainSchema(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        from_attributes=True,
    )

    type: TrainStatus
    title: str
    repeats: int | None
    approaches: int | None
    duration: int | None


class CreateTrainSchema(BaseTrainSchema):
    pass


class CreateTrainUserIdSchema(BaseTrainSchema):
    user_id: int


class TrainSchema(BaseTrainSchema):
    id: int
    user_id: int
    date: str
