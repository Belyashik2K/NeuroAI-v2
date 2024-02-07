from typing import Final
from aiogram import Router, F, types
from aiogram_i18n import LazyProxy, I18nContext

from ...database.models import User
from ...keyboards import inline, data

router: Final[Router] = Router(name=__name__)


@router.message(LazyProxy('buttons-admin'))
async def admin_panel(message: types.Message, user: User, i18n: I18nContext):
    await message.delete()
    await message.answer(
        i18n.messages.admin_panel(),
        reply_markup=await inline.admin()
    )


@router.callback_query(F.data == data.StartMenu.admin)
async def back(call: types.CallbackQuery, i18n: I18nContext):
    await call.message.edit_text(
        i18n.messages.admin_panel(),
        reply_markup=await inline.admin()
    )
