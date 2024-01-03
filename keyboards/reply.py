from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from texts import RB
from database.models import User

class ReplyKeyboards:

    async def get_start_keyboard(self, user: User) -> ReplyKeyboardMarkup:
        """
        Generate start keyboard.

        If user is admin, add admin button.
        
        Args:
            user (User): User object.
            
        Returns:
            ReplyKeyboardMarkup: Start keyboard.
        """
        k = ReplyKeyboardBuilder()

        neuro_choose = KeyboardButton(text=RB.neuro_choose)
        account = KeyboardButton(text=RB.my_account)
        stats = KeyboardButton(text=RB.stats)
        about = KeyboardButton(text=RB.about)

        k.row(neuro_choose)
        k.row(account, stats)
        k.row(about)

        if user.is_admin:
            admin = KeyboardButton(text=RB.admin)
            k.row(admin)

        return k.as_markup(resize_keyboard=True)
    
    async def stop_chatting_keyboard(self) -> ReplyKeyboardMarkup:
        """
        Generate stop chatting keyboard.
        
        Returns:
            ReplyKeyboardMarkup: Stop chatting keyboard.
        """
        k = ReplyKeyboardBuilder()
        k.row(KeyboardButton(text=RB.stop_chatting))
        return k.as_markup(resize_keyboard=True)