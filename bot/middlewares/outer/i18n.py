from typing import Optional, cast
from aiogram.types import User
from aiogram_i18n.managers import BaseManager

from ...database import database as db
from ...database.models import User as UDB

class UserManager(BaseManager):
    async def get_locale(
        self, event_from_user: Optional[User] = None, user: Optional[UDB] = None
    ) -> str:
        if user:
            return user.locale
        if event_from_user:
            return event_from_user.language_code or cast(str, self.default_locale)
        return cast(str, self.default_locale)

    async def set_locale(self, locale: str, user: UDB) -> None:
        await db.update_user(user_id=user.user_id, locale=locale)