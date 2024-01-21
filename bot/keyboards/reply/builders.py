from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram_i18n import LazyProxy
from aiogram_i18n.types import ReplyKeyboardMarkup, KeyboardButton

from ...database.models import User

class ReplyKeyboards:

    def menu(self, user: User) -> ReplyKeyboardMarkup:
        builder = ReplyKeyboardBuilder()

        neuro_choose = KeyboardButton(text=LazyProxy("buttons-neuro_choose"))
        account = KeyboardButton(text=LazyProxy("buttons-my_account"))
        stats = KeyboardButton(text=LazyProxy("buttons-stats"))
        about = KeyboardButton(text=LazyProxy("buttons-about"))

        builder.row(neuro_choose)
        builder.row(account, stats)
        builder.row(about)

        if user.is_admin:
            admin = KeyboardButton(text=LazyProxy("buttons-admin"))
            builder.row(admin)

        return builder.as_markup(resize_keyboard=True)

    def stop_chatting(self) -> ReplyKeyboardMarkup:
        builder = ReplyKeyboardBuilder()
        builder.row(KeyboardButton(text=LazyProxy("buttons-stop_chatting")))
        return builder.as_markup(resize_keyboard=True)