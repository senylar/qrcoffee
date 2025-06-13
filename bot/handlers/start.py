import logging
from aiogram import F
from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import ContentType

from Keyboards.default.services import request_contact_keyboard
from DataBase.models import Users
from Keyboards.default.sections import main_menu_keyboard
from DataBase.core import DBConnectorMdlw

router = Router()
router.message.middleware(DBConnectorMdlw())

class Registration(StatesGroup):
    name = State()
    phone = State()
    confirmation = State()



@router.message(Command("start"))
async def test_handler(message, state : FSMContext, session : DBConnectorMdlw):

    await message.answer("Добро пожаловать!")

    user = await Users.get_user_by_tg_id(session, int(message.from_user.id))

    if user:
        await message.answer("Вы уже зарегистрированы!")
        await message.answer("Вы можете начать использовать бота.", reply_markup=main_menu_keyboard())
        return
    await state.set_state(Registration.name)
    await message.answer('Введите ваше имя')


@router.message(Registration.name)
async def phone_handler(message, state : FSMContext):
    name = message.text
    await state.update_data(name=name)
    print(1)
    await state.set_state(Registration.phone)
    await message.answer('Предоставьте ваш номер телефона используя кнопку:',
                         reply_markup=request_contact_keyboard())

@router.message(Registration.phone, F.content_type == ContentType.CONTACT)
async def contact_handler(message, session : DBConnectorMdlw, state : FSMContext):
    contact = message.contact
    user_data = await state.get_data()
    name = user_data.get('name')
    print(contact)
    if contact:
        phone = contact.phone_number
        await message.answer(f"Спасибо, {name}! Ваш номер телефона: {phone}")
        # try:
        u = Users(telegram_id=message.from_user.id, name=name, phone=phone)
        await u.add(session)
        await message.answer("Вы успешно зарегистрированы!",reply_markup=main_menu_keyboard())
        # except Exception as e:
        #     logging.error(e)
        #     await message.answer(f"Произошла ошибка при добавлении пользователя, попробуйте позже.")
        #     return
        # Here you can add code to save the user data to the database
    else:
        await message.answer("Пожалуйста, предоставьте корректный номер телефона.")

