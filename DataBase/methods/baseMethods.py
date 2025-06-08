class BaseDbMethods:

    @classmethod
    async def get_by_id(cls, session, item_id: int):
        """Get an item by its ID."""
        return await session.get(cls, item_id)

    @classmethod
    async def get_all(cls, session):
        """Получить все записи."""
        result = await session.execute(
            cls.__table__.select()
        )
        return result.scalars().all()

    async def add(self, session):
        session.add(self)
        await session.commit()
        await session.refresh(self)
        return self

    async def update(self, session, **kwargs):
        """Обновить поля объекта и сохранить изменения."""
        for key, value in kwargs.items():
            setattr(self, key, value)
        await session.commit()
        await session.refresh(self)
        return self

    async def delete(self, session):
        """Удалить объект из базы данных."""
        await session.delete(self)
        await session.commit()
        return True
