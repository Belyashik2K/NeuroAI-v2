from typing import Final
from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram_i18n import I18nContext

from ...database import database
from ...database.models import User
from ...keyboards import inline, data
from ...fsm import *

router: Final[Router] = Router(name=__name__)

@router.callback_query(F.data==data.AdminPanel.change_neuro)
async def select_category(call: types.CallbackQuery, user: User, state: FSMContext, i18n: I18nContext):
    statuses = await database.get_neuro_statuses()
    await call.message.edit_text(i18n.messages.admin_neuro_statuses(**statuses), 
                                 reply_markup=inline.neuro_categories(True))

@router.callback_query(F.data.startswith(data.NeuroCategories.admin + data.NeuroCategories.start))
async def select_neuro(call: types.CallbackQuery, user: User, state: FSMContext, i18n: I18nContext):
    category = call.data.split("_")[3]
    await state.update_data(category=category)
    statuses = await database.get_neuro_statuses()
    await call.message.edit_text(i18n.messages.admin_neuro_statuses(**statuses), 
                                 reply_markup=inline.all_neuros(category))

@router.callback_query(F.data.startswith(data.Neuros.switch))
async def switch_neuro_status(call: types.CallbackQuery, user: User, state: FSMContext, i18n: I18nContext):
    neuro_name = call.data.split('_', 1)[1]
    data = await state.get_data()
    await database.switch_neuro_status(neuro_name=neuro_name)
    await call.answer(i18n.messages.admin_success())
    statuses = await database.get_neuro_statuses()
    await call.message.edit_text(i18n.messages.admin_neuro_statuses(**statuses), 
                                 reply_markup=inline.all_neuros(data['category']))
