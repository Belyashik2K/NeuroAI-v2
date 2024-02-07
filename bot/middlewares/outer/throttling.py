from cachetools import TTLCache

from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject


class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self):
        self.cache = TTLCache(maxsize=10_000, ttl=0.5)

    async def __call__(self,
                       handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
                       event: TelegramObject,
                       data: Dict[str, Any]) -> Any:
        user_event = event.message or event.callback_query
        if user_event.from_user.id in self.cache:
            return
        self.cache[user_event.from_user.id] = None
        return await handler(event, data)
