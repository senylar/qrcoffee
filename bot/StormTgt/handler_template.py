from aiogram import Router
from aiogram.filters import Command
from DataBase.core import DBConnectorMdlw

router = Router()
router.message.middleware(DBConnectorMdlw())



@router.message(Command("test"))
async def test_handler(message, session : DBConnectorMdlw):

    await message.answer("Test command received!")


