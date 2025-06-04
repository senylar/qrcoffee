# from aiogram import BaseMiddleware
# from aiogram.types import Message
# from typing import Callable, Awaitable, Dict, Any
# from .db_connection import get_db
#
#
# class CounterMiddleware(BaseMiddleware):
#
#     async def __call__(
#         self,
#         handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
#         event: Message,
#         data: Dict[str, Any]
#     ) -> Any:
#
#         async with get_db() as session:
#             # Assuming you want to increment a counter in the database
#
#             data['session'] = session
#             return await handler(event, data)
#
