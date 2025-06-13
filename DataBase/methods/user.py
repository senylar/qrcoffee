from sqlmodel import select

class UserMethods:

    @classmethod
    async def get_user_by_id(cls, session, user_id: int):
        return await session.get(cls, user_id)

    @classmethod
    async def get_user_by_tg_id(cls, session, tg_id: int):
        query = select(cls).where(cls.telegram_id == tg_id)
        result = await session.exec(query)
        return result.first()

    async def add(self, session):
        """Add a new user to the database."""
        session.add(self)
        await session.commit()
        await session.refresh(self)
        return self