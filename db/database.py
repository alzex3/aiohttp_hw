from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from settings import PG_DSN


Base = declarative_base()


class DatabaseSession:
    def __init__(self):
        self.session = None
        self.engine = None

    def __getattr__(self, name):
        return getattr(self.session, name)

    async def init(self):
        self.engine = create_async_engine(
            PG_DSN,
            echo=True,
        )

        self.session = sessionmaker(
            self.engine,
            expire_on_commit=False,
            class_=AsyncSession,
        )()

    async def create_all(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def drop_all(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)


db_session = DatabaseSession()
