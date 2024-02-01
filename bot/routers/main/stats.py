from typing import Final

from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram_i18n import I18nContext, LazyProxy

from ...database import database
from ...database.models import User
from ...keyboards import inline, data

router: Final[Router] = Router(name=__name__)

@router.message(F.text==LazyProxy("buttons-stats"))
async def stats(message: types.Message, user: User, state: FSMContext, i18n: I18nContext):
    await message.delete()
    await state.clear()
    await message.answer(i18n.messages.stats(**await database.get_stats()), reply_markup=inline.close())

@router.callback_query(F.data==data.StartMenu.stats)
async def stats(call: types.CallbackQuery, user: User, state: FSMContext, i18n: I18nContext):
    await state.clear()
    await call.message.edit_text(i18n.messages.stats(**await database.get_stats()), reply_markup=inline.close())

