from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from ...database import database


class UserMiddleware(BaseMiddleware):
    async def __call__(self,
                       handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
                       event: TelegramObject,
                       data: Dict[str, Any]) -> Any:
        user_event = event.message or event.callback_query

        user = await database.add_user(user_id=user_event.from_user.id,
                                       username=user_event.from_user.username,
                                       full_name=user_event.from_user.full_name,
                                       locale=user_event.from_user.language_code)

        if user.full_name != user_event.from_user.full_name or user.username != user_event.from_user.username:
            user = await database.update_user(user_id=user_event.from_user.id,
                                              username=user_event.from_user.username,
                                              full_name=user_event.from_user.full_name)

        await database.update_last_activity(user_id=user.user_id)
        data['user'] = user
        return await handler(event, data)
