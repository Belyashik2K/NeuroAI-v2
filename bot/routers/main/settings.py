from typing import Final

from aiogram import Router, F, types
from aiogram_i18n import I18nContext, LazyProxy

from ...database.models import User
from ...keyboards import inline, data

router: Final[Router] = Router(name=__name__)

@router.message(F.text == LazyProxy("buttons-settings"))
async def settings(message: types.Message, user: User, i18n: I18nContext):
    await message.answer(
        i18n.messages.settings(),
        reply_markup=inline.settings()
    )

@router.callback_query(F.data == data.Settings.set_language)
async def set_language(call: types.CallbackQuery, i18n: I18nContext):
    await call.message.edit_text(
        i18n.messages.choose_language(),
        reply_markup=inline.set_language()
    )