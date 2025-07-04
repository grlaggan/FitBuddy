from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio.session import AsyncSession
from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials

from src.database.init import init_db
from src.trains.crud import create_train
from src.trains.schemas import CreateTrainSchema, TrainSchema, CreateTrainUserIdSchema
from src.users.jwt import decode

Session = Annotated[AsyncSession, Depends(init_db.async_session)]
http_bearer = HTTPBearer()


async def create_train_depend(
    session: Session,
    train_data: CreateTrainSchema,
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(http_bearer)],
) -> TrainSchema:
    token = credentials.credentials
    payload = decode(token)

    train = await create_train(
        train=CreateTrainUserIdSchema(
            **train_data.model_dump(), user_id=int(payload["sub"])
        ),
        session=session,
    )

    return TrainSchema.model_validate(train)
