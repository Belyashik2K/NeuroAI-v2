from aiogram.filters import BaseFilter
from aiogram.types import Update

from ..database import database

class IsAdmin(BaseFilter):
    def __get_id(self, update: Update) -> int:
        try:
            return update.from_user.id
        except:
            return update.message.from_user.id

    async def __call__(self, update: Update) -> bool:
        user = await database.get_user(user_id=self.__get_id(update))
        return user.is_admin
    
class IsUserAdminInChat(BaseFilter):
    async def __call__(self, update: Update) -> bool:
        try:
            chat_id = update.chat.id
        except:
            chat_id = update.message.chat.id
        ids = [user.user.id for user in await update.bot.get_chat_administrators(chat_id=chat_id)]
        return update.from_user.id in ids