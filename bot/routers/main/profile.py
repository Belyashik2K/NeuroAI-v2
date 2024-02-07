from typing import Final

from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import any_state
from aiogram_i18n import I18nContext, LazyProxy

from ...database.models import User
from ...keyboards import inline, data

router: Final[Router] = Router(name=__name__)


@router.message(any_state, F.text == LazyProxy("buttons-my_account"))
async def profile(message: types.Message, user: User, state: FSMContext, i18n: I18nContext):
    await message.delete()
    await state.clear()
    data = {
        "name": message.from_user.mention_html(),
        "neuro_id": user.id,
        "request_counter": user.request_counter,
        "join_date": user.registered_at.strftime('%d.%m.%Y %H:%M'),
    }
    await message.answer(i18n.messages.my_profile(**data), reply_markup=inline.my_profile())


@router.callback_query(F.data == data.StartMenu.my_account)
async def back(call: types.CallbackQuery, i18n: I18nContext, user: User, state: FSMContext):
    await state.clear()
    data = {
        "name": call.from_user.mention_html(),
        "neuro_id": user.id,
        "request_counter": user.request_counter,
        "join_date": user.registered_at.strftime('%d.%m.%Y %H:%M'),
    }
    await call.message.edit_text(i18n.messages.my_profile(**data), reply_markup=inline.my_profile())
