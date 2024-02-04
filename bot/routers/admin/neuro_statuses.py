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
                                 reply_markup=await inline.neuro_categories(True))

@router.callback_query(data.AdminCategory.filter())
async def select_neuro(call: types.CallbackQuery, callback_data: data.AdminCategory,
                       user: User, state: FSMContext, i18n: I18nContext):
    await state.update_data(page=callback_data.page)
    _data = await state.get_data()
    page = _data['page']
    category = callback_data.name
    await state.update_data(category=category, page=page)
    statuses = await database.get_neuro_statuses()
    await call.message.edit_text(i18n.messages.admin_neuro_statuses(**statuses), 
                                 reply_markup=await inline.neuros(category=category,
                                                                  page=page,
                                                                  is_admin=True))

@router.callback_query(data.Switch.filter())
async def switch_neuro_status(call: types.CallbackQuery, callback_data: data.Switch,
                              user: User, state: FSMContext, i18n: I18nContext):
    neuro_name = callback_data.neuro_name
    data = await state.get_data()
    await database.switch_neuro_status(neuro_name=neuro_name)
    await call.answer(i18n.messages.admin_success())
    statuses = await database.get_neuro_statuses()
    await call.message.edit_text(i18n.messages.admin_neuro_statuses(**statuses), 
                                 reply_markup=await inline.neuros(category=data['category'],
                                                                  page=data['page'],
                                                                  is_admin=True))
