from typing import Final

from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram_i18n import I18nContext, LazyProxy

from ....database.models import User
from ....keyboards import inline, data
from ....filters import isNeuroActive

from ....fsm import *

router: Final[Router] = Router(name=__name__)


@router.message(F.text == LazyProxy("buttons-neuro_choose"))
async def neuro_category_choose(message: types.Message, user: User, state: FSMContext, i18n: I18nContext):
    await state.clear()
    await message.answer(i18n.messages.choose_neuro_category(), reply_markup=inline.neuro_categories())


@router.callback_query(F.data.in_([data.NeuroCategories.back, data.StartMenu.choose_neuro]))
async def neuro_category_choose_callback(call: types.CallbackQuery, user: User, state: FSMContext, i18n: I18nContext):
    await state.clear()
    await call.message.edit_text(i18n.messages.choose_neuro_category(), reply_markup=inline.neuro_categories())


@router.callback_query(F.data.startswith(data.NeuroCategories.start))
async def neuro_choose(call: types.CallbackQuery, user: User, state: FSMContext, i18n: I18nContext):
    await call.message.edit_text(i18n.messages.choose_neuro() + '\n\n' + LazyProxy(f'messages-{call.data}').data,
                                 reply_markup=inline.neuros(category=call.data))
    await state.update_data(category=call.data)


@router.callback_query(F.data.in_([data.Neuros.gpt, data.Neuros.claude,
                                   data.Neuros.google, data.Neuros.llama,
                                   data.Neuros.gemini, data.Neuros.mistral,
                                   data.Neuros.solar]),
                       isNeuroActive())
async def text_mode_choose(call: types.CallbackQuery, user: User, state: FSMContext, i18n: I18nContext):
    await state.clear()
    neuro = LazyProxy(f"buttons-{call.data.split('_')[1]}").data
    await call.message.edit_text(i18n.messages.mode(neuro=neuro), reply_markup=inline.mode())
    await state.update_data(neuro=call.data)


@router.callback_query(F.data == data.Mode.one_request)
async def one_request_mode(call: types.CallbackQuery, user: User, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()
    neuro = LazyProxy(f"buttons-{data['neuro'].split('_')[1]}").data
    mode = LazyProxy(f"buttons-{call.data.split('_', 1)[1]}").data
    await call.message.edit_text(
        i18n.messages.header(neuro=neuro, mode=mode) + "\n\n" + i18n.messages.one_request_mode(),
        reply_markup=inline.back(data['neuro']))
    await state.update_data(mode=call.data, message_id=call.message.message_id)
    await state.set_state(NeuroRequest.request)


@router.callback_query(F.data.in_([data.Neuros.stable, data.Neuros.playground,
                                   data.Neuros.midjourney, data.Neuros.dalle3,
                                   data.Neuros.enhance, data.Neuros.sdv,
                                   data.Neuros.tencentmaker, data.Neuros.midjourneyv6]),
                       isNeuroActive())
async def start_gen_image(call: types.CallbackQuery, user: User, state: FSMContext, i18n: I18nContext):
    neuro = LazyProxy(f"buttons-{call.data.split('_')[1]}").data

    choices = {
        data.Neuros.enhance: LazyProxy('messages-enchance_image', neuro=neuro).data,
        data.Neuros.sdv: LazyProxy('messages-sdv_video', neuro=neuro).data,
        data.Neuros.tencentmaker: LazyProxy('messages-tencentmaker', neuro=neuro).data
    }

    states = {
        data.Neuros.tencentmaker: NeuroRequest.tencentmaker,
        data.Neuros.midjourneyv6: NeuroRequest.midjourneyv6,
    }

    text = choices[call.data] if call.data in choices else i18n.messages.start_gen_image(neuro=neuro)

    await call.message.edit_text(text=text,
                                 reply_markup=inline.back(data.NeuroCategories.image),
                                 disable_web_page_preview=True)
    await state.update_data(neuro=call.data, message_id=call.message.message_id)
    await state.set_state(NeuroRequest.image_request if call.data not in states else states[call.data])

@router.callback_query(F.data.in_([data.Neuros.whisper, data.Neuros.bender]),
                       isNeuroActive())
async def start_gen_audio(call: types.CallbackQuery, user: User, state: FSMContext, i18n: I18nContext):
    neuro = LazyProxy(f"buttons-{call.data.split('_')[1]}").data

    choices = {
        data.Neuros.bender: LazyProxy('messages-bender_voice', neuro=neuro).data,
        data.Neuros.whisper: LazyProxy('messages-whisper_voice', neuro=neuro).data,
    }

    await call.message.edit_text(choices[call.data], reply_markup=inline.back(data.NeuroCategories.audio))
    await state.update_data(neuro=call.data, message_id=call.message.message_id)
    await state.set_state(NeuroRequest.bender if call.data == data.Neuros.bender else NeuroRequest.whisper)
