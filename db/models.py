from datetime import datetime

from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import update, delete
from sqlalchemy.future import select

from db.database import Base, db_session


class Advert(Base):
    __tablename__ = 'person'
    __mapper_args__ = {'eager_defaults': True}

    id = Column(Integer, primary_key=True)
    title = Column(String(25), nullable=False)
    description = Column(String(200), nullable=False)
    created_at = Column(Date, default=datetime.now())
    owner = Column(String(30), nullable=False)

    @classmethod
    async def get_all(cls):
        query = select(cls)
        results = await db_session.execute(query)

        return results.scalars().all()

    @classmethod
    async def get(cls, advert_id):
        query = select(cls).where(cls.id == advert_id)
        results = await db_session.execute(query)

        return results.scalars().first()

    @classmethod
    async def create(cls, advert):
        db_session.add(advert)
        await db_session.commit()

    @classmethod
    async def update(cls, advert_id, **kwargs):
        query = (
            update(cls)
            .where(cls.id == advert_id)
            .values(**kwargs)
            .execution_options(synchronize_session='fetch')
        )
        await db_session.execute(query)
        await db_session.commit()

    @classmethod
    async def delete(cls, advert_id):
        query = (
            delete(cls)
            .where(cls.id == advert_id)
            .execution_options(synchronize_session='fetch')
        )
        await db_session.execute(query)
        await db_session.commit()
