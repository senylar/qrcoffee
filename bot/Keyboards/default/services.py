from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def request_contact_keyboard() -> ReplyKeyboardMarkup:
    """
    Creates a keyboard with a button to request the user's contact information.
    """
    markup = ReplyKeyboardMarkup(keyboard=[],resize_keyboard=True, one_time_keyboard=True)
    markup.keyboard.append([KeyboardButton(text="Отправить номер телефона", request_contact=True)])

    return markup