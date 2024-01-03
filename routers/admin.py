from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from texts import RB, AT, IB, ET
from filters import IsAdmin
from database.models import User
from keyboards import inline
from fsm import AdminPanel
from initialization import bot
from database import database

admin_router = Router(name=__name__)

@admin_router.message(F.text==RB.admin, IsAdmin())
async def admin_panel(message: types.Message, user: User):
    await message.answer(AT.admin_menu, reply_markup=await inline.get_admin_keyboard())

@admin_router.callback_query(F.data==IB.Callback.AdminPanel.back)
async def back_to_start(call: types.CallbackQuery, user: User, state: FSMContext):
    await state.clear()
    await call.message.edit_text(AT.admin_menu, reply_markup=await inline.get_admin_keyboard())

@admin_router.callback_query(F.data==IB.Callback.AdminPanel.find_user)
async def find_user(call: types.CallbackQuery, user: User, state: FSMContext):
    await call.message.edit_text(AT.find_user, reply_markup=await inline.get_back_keyboard(IB.Callback.AdminPanel.back))
    await state.set_state(AdminPanel.find_user)
    await state.update_data(message_id=call.message.message_id)

@admin_router.message(AdminPanel.find_user, IsAdmin())
async def find_user_message(message: types.Message, user: User, state: FSMContext):
    data = await state.get_data()
    await message.delete()
    info = await database.get_user(message.text, True)
    if not info:
        await bot.edit_message_text(chat_id=message.chat.id, message_id=data['message_id'], text=ET.user_not_found, reply_markup=await inline.get_back_keyboard(IB.Callback.AdminPanel.back))
        return
    formatting = [
        f'<a href="tg://user?id={info.user_id}">{info.full_name}</a>',
        info.id,
        info.request_counter,
        info.registered_at.strftime('%d.%m.%Y %H:%M:%S'),
        ]
    await bot.edit_message_text(chat_id=message.chat.id, message_id=data['message_id'], text=AT.user_info.format(*formatting), reply_markup=await inline.get_user_keyboard(info))
    await state.clear()

@admin_router.callback_query(F.data==IB.Callback.AdminPanel.change_neuro, IsAdmin())
async def change_neuro(call: types.CallbackQuery, user: User, state: FSMContext):
    statuses = await database.get_neuro_statuses()
    await call.message.edit_text(AT.neuro_statuses.format(**statuses), reply_markup=await inline.get_all_neuros_keyboard())

@admin_router.callback_query(F.data.startswith(IB.Callback.Neuros.switch), IsAdmin())
async def switch_neuro(call: types.CallbackQuery, user: User, state: FSMContext):
    neuro_name = call.data.split('_', 1)[1]
    await database.switch_neuro_status(neuro_name=neuro_name)
    await call.answer(AT.success)
    statuses = await database.get_neuro_statuses()
    await call.message.edit_text(AT.neuro_statuses.format(**statuses), reply_markup=await inline.get_all_neuros_keyboard())

@admin_router.callback_query(F.data.startswith(IB.Callback.AdminPanel.ban), IsAdmin())
async def ban_user(call: types.CallbackQuery, user: User, state: FSMContext):
    user_id = int(call.data.split('_')[1])
    if user_id == call.from_user.id:
        await call.answer(ET.no)
        return
    user = await database.get_user(user_id=user_id)
    await database.update_user(user_id=user_id, is_banned=not user.is_banned)
    await call.answer(AT.success_edit)
    await call.message.edit_reply_markup(reply_markup=await inline.get_user_keyboard(await database.get_user(user_id=user_id)))

@admin_router.callback_query(F.data.startswith(IB.Callback.AdminPanel.admin), IsAdmin())
async def add_admin(call: types.CallbackQuery, user: User, state: FSMContext):
    user_id = int(call.data.split('_')[1])
    if user_id == call.from_user.id:
        await call.answer(ET.no)
        return
    user = await database.get_user(user_id=user_id)
    await database.update_user(user_id=user_id, is_admin=not user.is_admin)
    await call.answer(AT.success_edit)
    await call.message.edit_reply_markup(reply_markup=await inline.get_user_keyboard(await database.get_user(user_id=user_id)))

@admin_router.callback_query(F.data==IB.Callback.AdminPanel.maintenance, IsAdmin())
async def maintenance(call: types.CallbackQuery, user: User, state: FSMContext):
    await database.maintenance(True)
    await call.answer(AT.success_maintenance)
    await call.message.edit_text(AT.admin_menu, reply_markup=await inline.get_admin_keyboard())
