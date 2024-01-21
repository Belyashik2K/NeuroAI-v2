from ...config import config

from .texts import NotifyTexts as NT

class AdminNotify:

    def __init__(self) -> None:
        from ...loader import bot
        self.__bot = bot
        self.__admin_chat = config.admin_chat

    async def error_notify(self,
                           **kwargs
                           ) -> None:
        await self.__bot.send_message(chat_id=self.__admin_chat,
                               text=NT.error.format(**kwargs))
        
    async def new_user_notify(self,
                              neuro_id: int,
                              user_id: int,
                              full_name: str,
                              ) -> None:
        await self.__bot.send_message(chat_id=self.__admin_chat,
                               text=NT.new_user.format(user_id=user_id,
                                                       full_name=full_name,
                                                       neuro_id=neuro_id))
        
    async def new_chat_notify(self,
                            chat_id: int,
                            neuro_id: int
                            ) -> None:
        await self.__bot.send_message(chat_id=self.__admin_chat,
                               text=NT.new_chat.format(chat_id=chat_id,
                                                       neuro_id=neuro_id))    