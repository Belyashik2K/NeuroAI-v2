import asyncio

from aiogram.enums.content_type import ContentType as CT
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup
from aiogram.exceptions import TelegramRetryAfter, TelegramNotFound

from ..config import Config

from ..database.models import Mailing
from ..database import mailing_db as db
from ..texts import MT
from ..keyboards import MK

class MailingFunctions:

    def __init__(self) -> None:
        self._bot = Config.Bot.BOT_INSTANCE
        self._user_db = Config.UserDB.DB_INSTANCE

    async def get_menu_message(self) -> list[str, InlineKeyboardMarkup]:
        """Get mailing menu message by mailing info."""
        mailing_info = await db.get_mailing()

        types_names = {
            CT.AUDIO: "Аудиозапись",
            CT.VIDEO: "Видеозапись",
            CT.VOICE: "Голосовое сообщение",
            CT.ANIMATION: "GIF-анимация",
            CT.PHOTO: "Фотография",
            CT.DOCUMENT: "Документ",
            CT.VIDEO_NOTE: "Видеосообщение",
            CT.TEXT: "Текст"
        }

        users_count = await self._user_db.get_users_count()

        if mailing_info.content_type == CT.TEXT:
            vars_ = [users_count, mailing_info.alive_users, mailing_info.died_users,
                     types_names[mailing_info.content_type], mailing_info.text,
                     mailing_info.media,
                     mailing_info.button_text, mailing_info.button_link,
                     mailing_info.link_preview]
            return MT.mailing_menu_types["no_media"].format(*vars_), await MK.mailing_menu_keyboard()
        elif mailing_info.content_type in [CT.AUDIO, CT.VIDEO, CT.VOICE, CT.ANIMATION, CT.PHOTO, CT.DOCUMENT]:
            vars_ = [users_count, mailing_info.alive_users, mailing_info.died_users,
                     types_names[mailing_info.content_type], mailing_info.text,
                     mailing_info.media, mailing_info.button_text, 
                     mailing_info.button_link]
            return MT.mailing_menu_types["with_media"].format(*vars_), await MK.mailing_menu_keyboard(is_media=True)
        elif mailing_info.content_type == CT.VIDEO_NOTE:
            vars_ = [users_count, mailing_info.alive_users, mailing_info.died_users,
                     types_names[mailing_info.content_type], mailing_info.media,
                     mailing_info.button_text, mailing_info.button_link]
            return MT.mailing_menu_types["video_note"].format(*vars_), await MK.mailing_menu_keyboard(is_video_note=True)
    
    async def send_mailing_message(self, 
                                   user_id: int,
                                   mailing_info: Mailing,
                                   content_type: str,
                                   ) -> None:
        """Send mailing message to user."""
        content_types = {
            CT.AUDIO: self._bot.send_audio,
            CT.VIDEO: self._bot.send_video,
            CT.VOICE: self._bot.send_voice,
            CT.ANIMATION: self._bot.send_animation,
            CT.PHOTO: self._bot.send_photo,
            CT.DOCUMENT: self._bot.send_document,
            CT.VIDEO_NOTE: self._bot.send_video_note,
            CT.TEXT: self._bot.send_message
        }

        k = InlineKeyboardBuilder()

        if mailing_info.button_text != "Не установлен" and mailing_info.button_link != "Не установлена":
            k.button(text=mailing_info.button_text, url=mailing_info.button_link)

        if content_type not in [CT.TEXT, CT.VIDEO_NOTE]:
            if mailing_info.text != "Не установлен":
                await content_types[content_type](user_id, mailing_info.media, caption=mailing_info.text, reply_markup=k.as_markup())
            else:
                await content_types[content_type](user_id, mailing_info.media, reply_markup=k.as_markup())
        elif content_type == CT.TEXT:
            await content_types[content_type](user_id, mailing_info.text, reply_markup=k.as_markup(), disable_web_page_preview=mailing_info.link_preview)
        elif content_type == CT.VIDEO_NOTE:
            await content_types[content_type](user_id, mailing_info.media, reply_markup=k.as_markup())
        
    async def mailing(self, 
                      mailing_info: Mailing,
                      content_type: str,
                      users: list[int],
                      chat_id: int,
                      message_id: int,
                      ) -> None:
        """Send mailing to users."""
        from ..texts import MT

        alive_users = died_users = 0

        for user_id in users:
            try:
                await self.send_mailing_message(user_id, mailing_info, content_type)
                await asyncio.sleep(0.7)
                alive_users += 1
            except TelegramRetryAfter as e:
                await asyncio.sleep(e.retry_after)
                await self.send_mailing_message(user_id, mailing_info, content_type)
                alive_users += 1
            except Exception as e:
                died_users += 1

            try:
                await self._bot.edit_message_text(MT.mailing_start.format(alive_users, died_users), chat_id, message_id)
            except TelegramRetryAfter as e:
                await asyncio.sleep(e.retry_after)
                await self._bot.edit_message_text(MT.mailing_start.format(alive_users, died_users), chat_id, message_id)  
        await self._bot.edit_message_text(MT.mailing_end.format(alive_users, died_users), chat_id, message_id)
        
        return alive_users, died_users
