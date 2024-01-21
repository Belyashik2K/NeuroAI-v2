from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from aiogram_i18n import LazyProxy

from ...database import database

class MaintenanceMiddleware(BaseMiddleware):
    async def __call__(self, 
                       handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]], 
                       event: TelegramObject, 
                       data: Dict[str, Any]) -> Any:
        user_event = event.message or event.callback_query
        user = await database.get_user(user_id=user_event.from_user.id)
        maintenance = await database.maintenance()
        if not user.is_admin and maintenance:
            await user_event.answer(LazyProxy('errors-maintenance').data)
            return
        return await handler(event, data)
