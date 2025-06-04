from aiogram import Router
from aiogram.filters import Command
from DataBase.core import CounterMiddleware
from DataBase.models.models import User

router = Router()
router.message.middleware(CounterMiddleware())



@router.message(Command("test"),)
async def test_handler(message, session : CounterMiddleware):
    u = User(username="testuser", email="s@s.s", phone="+1234567890", full_name="Test User")
    print(u)
    res = await u.add(session)
    print(res)
    u = await u.get_user_by_id(session, 0)
    await message.answer("Test command received!")


