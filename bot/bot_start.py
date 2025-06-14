
import asyncio
from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import Command
from StormTgt.handlers_autoadd import auto_add_h

TOKEN = "7528228515:AAGdm7EioE6fZvL1WoGh9TCKjZBGHQcUaz4"

bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()

@router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Привет!")

dp.include_router(router)

async def main():
    auto_add_h(dp)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())