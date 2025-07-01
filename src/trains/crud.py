from sqlalchemy.ext.asyncio.session import AsyncSession
from datetime import datetime, timezone

from src.trains.schemas import CreateTrainUserIdSchema
from src.trains.models import TrainModel


async def create_train(
    session: AsyncSession, train: CreateTrainUserIdSchema
) -> TrainModel:
    now = datetime.now(tz=timezone.utc)
    str_now = now.strftime("%Y-%m-%d")

    train_obj = TrainModel(
        type=train.type,
        title=train.title,
        repeats=train.repeats,
        approaches=train.approaches,
        duration=train.duration,
        date=str_now,
        user_id=train.user_id,
    )
    session.add(train_obj)
    await session.commit()
    await session.refresh(train_obj)

    return train_obj
