from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

from .buttons import MailingButtons as b, MailingData as d
from ..config import Config

class MailingKeyboards:

    async def back_to_admin_keyboard(self, as_markup = True):
        kb = InlineKeyboardBuilder()
        kb.button(text=b.Back.back_to_admin, callback_data=Config.admin_menu_data)
        return kb.as_markup() if as_markup else InlineKeyboardButton(text=b.Back.back_to_admin, callback_data=Config.admin_menu_data)
    
    async def back_to_mailing_keyboard(self, as_markup = True):
        kb = InlineKeyboardBuilder()
        kb.button(text=b.Back.back_to_mailing, callback_data=d.Back.back_to_mailing)
        return kb.as_markup() if as_markup else InlineKeyboardButton(text=b.Back.back_to_mailing, callback_data=d.Back.back_to_mailing)
    
    async def mailing_menu_keyboard(self, is_media: bool = False, is_video_note: bool = False):
        start = InlineKeyboardButton(text=b.Menu.start, callback_data=d.Menu.start)
        view_message = InlineKeyboardButton(text=b.Menu.view_message, callback_data=d.Menu.view_message)
        button = InlineKeyboardButton(text=b.Menu.button, callback_data=d.Menu.button)
        text = InlineKeyboardButton(text=b.Menu.text, callback_data=d.Menu.text)
        media = InlineKeyboardButton(text=b.Menu.media, callback_data=d.Menu.media)
        disable_webpage_preview = InlineKeyboardButton(text=b.Menu.disable_webpage_preview, callback_data=d.Menu.disable_webpage_preview)
        reset = InlineKeyboardButton(text=b.Menu.reset, callback_data=d.Menu.reset)

        kb = InlineKeyboardBuilder()

        kb.row(start)
        kb.row(view_message, button)

        if is_video_note:
            kb.row(media)
        else:
            kb.row(text, media)

        if not is_media and not is_video_note:
            kb.row(disable_webpage_preview)

        kb.row(reset)
        kb.row(await self.back_to_admin_keyboard(False))

        return kb.as_markup()
    
    async def mailing_button_edit_keyboard(self):

        kb = InlineKeyboardBuilder()

        buttons = [
            InlineKeyboardButton(text=b.EditButton.button_text, callback_data=d.EditButton.button_text),
            InlineKeyboardButton(text=b.EditButton.button_link, callback_data=d.EditButton.button_link),
            InlineKeyboardButton(text=b.Back.back_to_mailing, callback_data=d.Back.back_to_mailing)
        ]
        
        kb.row(*buttons[:2])
        kb.row(buttons[2])

        return kb.as_markup()

    async def mailing_sure_keyboard(self):
        kb = InlineKeyboardBuilder()

        kb.button(text=b.StartMailing.sure, callback_data=d.StartMailing.sure)
        kb.add(await self.back_to_mailing_keyboard(False))

        return kb.as_markup()