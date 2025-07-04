from sqlalchemy.ext.asyncio.engine import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession, async_sessionmaker

from src import sets


class InitDB:
    def __init__(self):
        self.engine = create_async_engine(sets.db.url)
        self.get_session = async_sessionmaker(self.engine)

    async def async_session(self):
        async with self.get_session() as session:
            yield session
