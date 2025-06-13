from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class MainMenuButtons:
    qr_code ="Qr-код"
    profile = "Профиль"
    promotions = "Акции"
    history = "История операций"
    about_us = "О нас"
    balance = "Баланс"



def main_menu_keyboard() -> ReplyKeyboardMarkup:
    """
    Создаёт клавиатуру главного меню с кнопками для разных разделов.
    """
    keyboard = [
        [
            KeyboardButton(text=MainMenuButtons.qr_code),
            KeyboardButton(text=MainMenuButtons.profile)
        ],
        [
            KeyboardButton(text=MainMenuButtons.promotions)
        ],
        [
            KeyboardButton(text=MainMenuButtons.history),
            KeyboardButton(text=MainMenuButtons.about_us)
        ],
        [
            KeyboardButton(text=MainMenuButtons.balance)
        ]
    ]

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        one_time_keyboard=True
    )