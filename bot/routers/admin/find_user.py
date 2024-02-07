from typing import Final
from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram_i18n import I18nContext

from ...database import database
from ...database.models import User
from ...keyboards import inline, data
from ...fsm import *

router: Final[Router] = Router(name=__name__)


@router.callback_query(F.data == data.AdminPanel.find_user)
async def find_user(call: types.CallbackQuery, user: User, state: FSMContext, i18n: I18nContext):
    await call.message.edit_text(i18n.messages.admin_find_user(),
                                 reply_markup=inline.back(data.StartMenu.admin))
    await state.set_state(AdminPanel.find_user)
    await state.update_data(message_id=call.message.message_id)


@router.message(AdminPanel.find_user)
async def find_user_message(message: types.Message, user: User, state: FSMContext, i18n: I18nContext):
    state_data = await state.get_data()
    await message.delete()
    info = await database.get_user(message.text, True)
    if not info:
        await message.bot.edit_message_text(chat_id=message.chat.id,
                                            message_id=state_data['message_id'],
                                            text=i18n.errors.user_not_found(),
                                            reply_markup=inline.back(data.StartMenu.admin))
        return
    formatting = {
        'name': f'<a href="tg://user?id={info.user_id}">{info.full_name}</a>',
        'neuro_id': info.id,
        'request_counter': info.request_counter,
        'join_date': info.registered_at.strftime('%d.%m.%Y %H:%M:%S'),
    }
    await message.bot.edit_message_text(chat_id=message.chat.id,
                                        message_id=state_data['message_id'],
                                        text=i18n.messages.admin_user_info(**formatting),
                                        reply_markup=await inline.user_actions(info, message))
    await state.clear()


@router.callback_query(data.BanUser.filter())
async def ban_user(call: types.CallbackQuery, callback_data: data.BanUser,
                   user: User, state: FSMContext, i18n: I18nContext):
    user_id = callback_data.user_id
    if user_id == call.from_user.id:
        await call.answer(i18n.errors.no())
        return
    user = await database.get_user(user_id=user_id)
    new = await database.update_user(user_id=user_id, is_banned=not user.is_banned)
    await call.answer(i18n.messages.admin_success_edit())
    await call.message.edit_reply_markup(reply_markup=await inline.user_actions(new, call))


@router.callback_query(data.AdminUser.filter())
async def add_admin(call: types.CallbackQuery, callback_data: data.AdminUser,
                    user: User, state: FSMContext, i18n: I18nContext):
    user_id = callback_data.user_id
    if user_id == call.from_user.id:
        await call.answer(i18n.errors.no())
        return
    user = await database.get_user(user_id=user_id)
    new = await database.update_user(user_id=user_id, is_admin=not user.is_admin)
    await call.answer(i18n.messages.admin_success_edit())
    await call.message.edit_reply_markup(reply_markup=await inline.user_actions(new, call))
