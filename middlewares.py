from aiogram import BaseMiddleware, Dispatcher
from aiogram.types import TelegramObject

from typing import Any, Callable, Dict, Awaitable
from datetime import datetime
from cachetools import TTLCache

from texts import ET
from database import database as db

class UserMiddleware(BaseMiddleware):
    async def __call__(self, 
                       handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]], 
                       event: TelegramObject, 
                       data: Dict[str, Any]) -> Any:
        user = await db.add_user(user_id=event.from_user.id, 
                                username=event.from_user.username, 
                                full_name=event.from_user.full_name)
        if user.is_banned:
            await event.answer(ET.user_banned)
            return
        if user.full_name != event.from_user.full_name or user.username != event.from_user.username:
            await db.update_user(user_id=user.user_id, 
                                 username=event.from_user.username, 
                                 full_name=event.from_user.full_name)
        await db.update_user(user_id=user.user_id, last_activity=datetime.now())
        data['user'] = user
        return await handler(event, data)
    
class ChatMiddleware(BaseMiddleware):
    async def __call__(self,
                          handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]], 
                          event: TelegramObject, 
                          data: Dict[str, Any]) -> Any:
        try:
            chat_id = event.chat.id
        except:
            chat_id = event.message.chat.id
        chat = await db.add_chat(chat_id=chat_id)
        data['chat'] = chat
        await db.update_chat(chat_id=chat.chat_id, last_activity=datetime.now())
        return await handler(event, data)
    
class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self):
        self.cache = TTLCache(maxsize=10_000, ttl=0.5)

    async def __call__(self, 
                       handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]], 
                       event: TelegramObject, 
                       data: Dict[str, Any]) -> Any:
        if event.chat.id in self.cache:
            return
        self.cache[event.chat.id] = None
        return await handler(event, data)
    
class MaintenanceMiddleware(BaseMiddleware):
    async def __call__(self, 
                       handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]], 
                       event: TelegramObject, 
                       data: Dict[str, Any]) -> Any:
        user = await db.get_user(user_id=event.from_user.id)
        maintenance = await db.maintenance()
        if not user.is_admin and maintenance:
            await event.answer(ET.maintenance)
            return
        return await handler(event, data)
