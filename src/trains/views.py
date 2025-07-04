from typing import Annotated

from fastapi import APIRouter, Depends
from src.trains.schemas import TrainSchema
from src.trains.dependencies import create_train_depend

router = APIRouter(prefix="/trains", tags=["trains"])


@router.post(
    "/",
    response_model=TrainSchema,
    summary="Create train schema",
    response_model_exclude_none=True,
)
async def create_train_schema(
    train: Annotated[TrainSchema, Depends(create_train_depend)],
):
    return train
