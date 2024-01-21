from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from datetime import datetime

from ...database import database

class ChatMiddleware(BaseMiddleware):
    async def __call__(self,
                          handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]], 
                          event: TelegramObject, 
                          data: Dict[str, Any]) -> Any:
        try:
            chat_id = event.chat.id
        except:
            chat_id = event.message.chat.id
        chat = await database.add_chat(chat_id=chat_id)
        data['chat'] = chat
        await database.update_chat(chat_id=chat.chat_id, last_activity=datetime.now())
        return await handler(event, data)