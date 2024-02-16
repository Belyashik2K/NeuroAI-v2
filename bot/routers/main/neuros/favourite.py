from typing import Final

from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import any_state
from aiogram_i18n import I18nContext, LazyProxy

from ....database import database
from ....database.models import User
from ....keyboards import inline, data
from ....filters import isNeuroActive
from ....enums import *
from ....fsm import *

router: Final[Router] = Router(name=__name__)


@router.callback_query(F.data == data.StartMenu.favourite)
async def favourite_neuro_list(call: types.CallbackQuery, user: User, state: FSMContext, i18n: I18nContext):
    await state.clear()
    
    await state.update_data(page=1)
    data = await state.get_data()
    page = data.get('page', 1)
    
    text = i18n.messages.favourite_neuro() if await database.favourite_count(user_id=user.user_id) else i18n.messages.no_favourite(select_neuro=LazyProxy('buttons-neuro_choose').data,
                                                                                                                                   favourite_button=LazyProxy("buttons-add_fav").data)
    
    await call.message.edit_text(text, reply_markup=await inline.favourite(user_id=user.user_id,
                                                                            page=page))

    await state.update_data(from_fav=True)

@router.callback_query(data.FavouritePagination.filter())
async def favourite_neuro_list_pagination(call: types.CallbackQuery, callback_data: data.FavouritePagination,
                                        user: User, state: FSMContext, i18n: I18nContext):
        await state.update_data(page=callback_data.page)
        data = await state.get_data()
        page = data.get('page', 1)
        
        text = i18n.messages.favourite_neuro() if await database.favourite_count(user_id=user.user_id) else i18n.messages.no_favourite(select_neuro=LazyProxy('buttons-neuro_choose').data,
                                                                                                                                   favourite_button=LazyProxy("buttons-add_fav").data)
    
        await call.message.edit_text(text, reply_markup=await inline.favourite(user_id=user.user_id,
                                                                                page=page))
        await state.update_data(from_fav=True)
        
@router.callback_query(data.Favourite.filter())
async def favourite_neuro(call: types.CallbackQuery, callback_data: data.Favourite,
                          user: User, state: FSMContext, i18n: I18nContext):
    
    data = await state.get_data()
    page = data.get('page', 1)
    
    result = await database.favourite_actions(user_id=user.user_id, 
                                     neuro_name=callback_data.neuro_name,
                                     action=callback_data.action)
    
    types = {
        Category.TEXT: inline.mode(page=page, 
                                   neuro_name=callback_data.neuro_name, 
                                   in_favourite=result,
                                   from_fav=data.get('from_fav', False)),
    }
    
    if callback_data.category in types:
        await call.message.edit_reply_markup(inline_message_id=call.inline_message_id,
                                             reply_markup=types[callback_data.category])
    else:
        keyboard = inline.image_or_voice(category=callback_data.category,
                                        neuro_name=callback_data.neuro_name,
                                        in_favourite=result,
                                        from_fav=data.get('from_fav', False),
                                        page=page)
        await call.message.edit_reply_markup(inline_message_id=call.inline_message_id,
                                            reply_markup=keyboard)