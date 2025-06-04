

class BaseDbMethods:

    @classmethod
    async def get_by_id(cls, session, item_id: int):
        """Get an item by its ID."""
        return await session.get(cls, item_id)

    async def add(self, session):
        session.add(self)
        await session.commit()
        await session.refresh(self)
        return self

