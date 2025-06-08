from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage

from DataBase.core import CounterMiddleware

router = Router()
router.message.middleware(CounterMiddleware())

class Registration(StatesGroup):
    name = State()
    phone = State()



@router.message(Command("start"))
async def test_handler(message, session : CounterMiddleware):

    await message.answer("Добро пожаловать!")
    # await


### кароче надо подумать о бд еще раз. все провалидировать и продумать