from config import Config
from initialization import bot
from texts import AT

class AdminNotify:

    def __init__(self) -> None:
        self.__admin_chat = Config.admin_chat

    async def error_notify(self,
                           **kwargs
                           ) -> None:
        await bot.send_message(chat_id=self.__admin_chat,
                               text=AT.error.format(**kwargs))
        
    async def new_user_notify(self,
                              neuro_id: int,
                              user_id: int,
                              full_name: str,
                              ) -> None:
        await bot.send_message(chat_id=self.__admin_chat,
                               text=AT.new_user.format(user_id=user_id,
                                                       full_name=full_name,
                                                       neuro_id=neuro_id))