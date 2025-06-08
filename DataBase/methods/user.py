

class UserMethods:

    @classmethod
    async def get_user_by_id(cls, session, user_id: int):
        return await session.get(cls, user_id)

    async def add(self, session):
        """Add a new user to the database."""
        session.add(self)
        await session.commit()
        await session.refresh(self)
        return self