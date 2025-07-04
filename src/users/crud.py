from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy import select

from src.database import UserModel
from src.users.schemas import CreateUserSchema
from src.users.password import hash_password


async def create_user(user_data: CreateUserSchema, session: AsyncSession) -> UserModel:
    new_user = UserModel(
        id=user_data.id,
        username=user_data.username,
        password=hash_password(user_data.password),
    )

    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)

    return new_user


async def get_user_by_id(user_id: int, session: AsyncSession) -> type[UserModel] | None:
    user = await session.get(UserModel, user_id)

    if not user:
        return None

    session.add(user)
    await session.commit()
    await session.refresh(user)

    return user


async def get_user_by_username(
    username: str, session: AsyncSession
) -> type[UserModel] | None:
    query = select(UserModel).where(UserModel.username == username)

    result = await session.execute(query)
    user = result.scalar_one_or_none()

    return user
