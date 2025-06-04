from typing import AsyncGenerator, final
from contextlib import asynccontextmanager

import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from config import DB_URL


# Create an asynchronous engine
engine = create_async_engine(DB_URL, echo=True)
# Create a session factory
SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,

)

@asynccontextmanager
async def get_db():
    """
    Получить сессию базы данных, автоматически закрывая её после использования.
    Используйте через async with:
        async with get_db() as session:
            ...
    """
    async with SessionLocal() as session:
        yield session

from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Awaitable, Dict, Any


class CounterMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:

        async with get_db() as session:
            # Assuming you want to increment a counter in the database

            data['session'] = session
            return await handler(event, data)

