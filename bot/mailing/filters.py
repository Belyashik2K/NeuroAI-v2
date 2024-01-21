from aiogram.filters import BaseFilter
from aiogram.types import Update

from .config import Config

class IsAdmin(BaseFilter):
    def __init__(self) -> None:
        self._user_db = Config.UserDB.DB_INSTANCE

    async def __call__(self, update: Update) -> bool:
        admin_list = await self._user_db.get_admins()
        return update.from_user.id in admin_list
