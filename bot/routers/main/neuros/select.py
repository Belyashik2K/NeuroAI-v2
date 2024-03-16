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


@router.message(any_state, F.text == LazyProxy("buttons-neuro_choose"))
async def neuro_category_choose(message: types.Message, user: User, state: FSMContext, i18n: I18nContext):
    await message.delete()
    await state.clear()
    await message.answer(i18n.messages.choose_neuro_category(), reply_markup=await inline.neuro_categories())


@router.callback_query(F.data == data.StartMenu.choose_neuro)
async def neuro_category_choose_callback(call: types.CallbackQuery, user: User, state: FSMContext, i18n: I18nContext):
    await state.clear()
    await call.message.edit_text(i18n.messages.choose_neuro_category(), reply_markup=await inline.neuro_categories())


@router.callback_query(data.Category.filter())
async def neuro_choose(call: types.CallbackQuery, callback_data: data.Category,
                       user: User, state: FSMContext, i18n: I18nContext):
    await state.update_data(page=callback_data.page)
    _data = await state.get_data()
    page = _data['page']
    await call.message.edit_text(
        i18n.messages.choose_neuro() + '\n\n' + LazyProxy(f'messages-{call.data.rsplit("_", 1)[0]}').data,
        reply_markup=await inline.neuros(category=callback_data.name, page=page))
    await state.update_data(category=callback_data.name, page=page)


@router.callback_query(data.Neuro.filter(F.category == Category.TEXT), isNeuroActive())
async def text_mode_choose(call: types.CallbackQuery, callback_data: data.Neuro,
                           user: User, state: FSMContext, i18n: I18nContext):
    _data = await state.get_data()
    try:
        page = _data['page']
    except KeyError:
        page = 1
        
    in_favorite = await database.is_favourite(user.user_id, callback_data.name)
        
    await state.clear()
    neuro = LazyProxy(f"buttons-{callback_data.name}").data
    await call.message.edit_text(i18n.messages.mode(neuro=neuro), reply_markup=inline.mode(page=page,
                                                                                           neuro_name=callback_data.name,
                                                                                           in_favourite=in_favorite,
                                                                                           from_fav=_data.get('from_fav', False)))
    await state.update_data(neuro=callback_data.name, provider=callback_data.provider)


@router.callback_query(data.Mode.filter(F.type_ == Mode.ONE))
async def one_request_mode(call: types.CallbackQuery, callback_data: data.Mode,
                           user: User, state: FSMContext, i18n: I18nContext):
    _data = await state.get_data()
    neuro = LazyProxy(f"buttons-{_data['neuro']}").data
    mode = LazyProxy(f"buttons-{callback_data.type_}").data
    neuro_info = await database.get_neuro(_data['neuro'])
    await call.message.edit_text(
        i18n.messages.header(neuro=neuro, mode=mode) + "\n\n" + i18n.messages.one_request_mode(),
        reply_markup=inline.back(callback_data=data.Neuro(provider=neuro_info.provider,
                                                          category=neuro_info.category,
                                                          name=neuro_info.code_name).pack()))
    await state.update_data(mode=callback_data.type_, message_id=call.message.message_id)
    await state.set_state(NeuroRequest.request)


@router.callback_query(data.Neuro.filter(F.category == Category.IMAGE), isNeuroActive())
async def start_gen_image(call: types.CallbackQuery, callback_data: data.Neuro,
                          user: User, state: FSMContext, i18n: I18nContext):
    _data = await state.get_data()
    try:
        page = _data['page']
    except KeyError:
        page = 1
    neuro = LazyProxy(f"buttons-{callback_data.name}").data

    choices = {
        Neuro.ENHANCE: LazyProxy('messages-enchance_image', neuro=neuro).data,
        Neuro.VIDEODIFFUSION: LazyProxy('messages-sdv_video', neuro=neuro).data,
        Neuro.TENCENTMAKER: LazyProxy('messages-tencentmaker', neuro=neuro).data
    }

    states = {
        Neuro.TENCENTMAKER: NeuroRequest.tencentmaker,
        Neuro.MIDJOURNEYV6: NeuroRequest.midjourneyv6,
        Neuro.ENHANCE: NeuroRequest.enchance_image
    }

    text = choices[callback_data.name] if callback_data.name in choices else i18n.messages.start_gen_image(neuro=neuro)
    if not call.message.photo and not call.message.video and not call.message.reply_to_message:
        await call.message.edit_text(text=text,
                                     reply_markup=inline.image_or_voice(category=Category.IMAGE,
                                                                        neuro_name=callback_data.name,
                                                                        in_favourite=await database.is_favourite(user.user_id, callback_data.name),
                                                                        page=page,
                                                                        from_fav=_data.get('from_fav', False)),
                                     disable_web_page_preview=True)
        await state.update_data(neuro=callback_data.name,
                                provider=callback_data.provider,
                                message_id=call.message.message_id)
    else:
        await call.answer()
        m = await call.bot.send_message(chat_id=call.message.chat.id,
                                        text=text,
                                        reply_markup=inline.image_or_voice(category=Category.IMAGE,
                                                                            neuro_name=callback_data.name,
                                                                            in_favourite=await database.is_favourite(user.user_id, callback_data.name),
                                                                            page=page,
                                                                            from_fav=_data.get('from_fav', False)),
                                        disable_web_page_preview=True)
        await state.update_data(neuro=callback_data.name,
                                provider=callback_data.provider,
                                message_id=m.message_id)
    await state.set_state(
        NeuroRequest.image_request if callback_data.name not in states else states[callback_data.name])


@router.callback_query(data.Neuro.filter(F.category == Category.AUDIO), isNeuroActive())
async def start_gen_audio(call: types.CallbackQuery, callback_data: data.Neuro,
                          user: User, state: FSMContext, i18n: I18nContext):
    _data = await state.get_data()
    neuro = LazyProxy(f"buttons-{callback_data.name}").data

    choices = {
        Neuro.BENDER: LazyProxy('messages-bender_voice', neuro=neuro).data,
        Neuro.WHISPER: LazyProxy('messages-whisper_mode', neuro=neuro).data,
    }

    if Neuro.BENDER == callback_data.name:
        await call.message.edit_text(choices[callback_data.name],
                                    reply_markup=inline.image_or_voice(category=Category.AUDIO,
                                                                        neuro_name=callback_data.name,
                                                                        in_favourite=await database.is_favourite(user.user_id, callback_data.name),
                                                                        page=_data.get('page', 1),
                                                                        from_fav=_data.get('from_fav', False)))
        await state.set_state(NeuroRequest.bender)
    else:
        await call.message.edit_text(choices[callback_data.name],
                                     reply_markup=inline.whisper_modes())
    await state.update_data(neuro=callback_data.name, message_id=call.message.message_id)


@router.callback_query(data.Mode.filter(F.type_.in_([Task.TRANSCRIBE, Task.TRANSLATE])))
async def await_whisper(call: types.CallbackQuery, state: FSMContext, i18n: I18nContext, callback_data: data.Mode):
    _data = await state.get_data()
    
    data_ = {
        'neuro': LazyProxy(f'buttons-{_data["neuro"]}').data,
        'mode': LazyProxy(f'buttons-{callback_data.type_}').data
    }
    
    neuro_info = await database.get_neuro(_data['neuro'])
    await call.message.edit_text(i18n.messages.whisper_voice(**data_), 
                                 reply_markup=inline.back(data.Neuro(provider=neuro_info.provider,
                                                                    category=neuro_info.category,
                                                                    name=neuro_info.code_name).pack()))
    await state.set_state(NeuroRequest.whisper)
    await state.update_data(message_id=call.message.message_id, w_mode=callback_data.type_)