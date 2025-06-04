from aiogram import Router
from aiogram.filters import Command
from DataBase.core import CounterMiddleware

router = Router()
router.message.middleware(CounterMiddleware())



@router.message(Command("test"))
async def test_handler(message, session : CounterMiddleware):

    await message.answer("Test command received!")


