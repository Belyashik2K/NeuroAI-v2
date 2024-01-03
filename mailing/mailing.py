from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.enums.content_type import ContentType as CT

from .config import Config
from .database import mailing_db as db
from .texts import MT
from .keyboards import MK, MD
from .fsm import MailingState
from .utils import sender
from .filters import IsAdmin

mailing_router = Router(name=__name__)

@mailing_router.callback_query(IsAdmin(), F.data==Config.mailing_button_data)
async def mailing_menu(call: types.CallbackQuery, state: FSMContext):
    await state.clear()
    mailing_info = await sender.get_menu_message()
    await call.message.edit_text(text=mailing_info[0], reply_markup=mailing_info[1], disable_web_page_preview=True)

@mailing_router.callback_query(IsAdmin(), F.data==MD.Menu.disable_webpage_preview)
async def disable_webpage_preview(call: types.CallbackQuery, state: FSMContext):
    await db.update_link_preview()
    await call.answer(MT.done, show_alert=True)
    mailing_info = await sender.get_menu_message()
    await call.message.edit_text(text=mailing_info[0], reply_markup=mailing_info[1], disable_web_page_preview=True)

@mailing_router.callback_query(IsAdmin(), F.data==MD.Menu.reset)
async def reset(call: types.CallbackQuery, state: FSMContext):
    await db.reset_mailing()
    await call.answer(MT.done, show_alert=True)
    mailing_info = await sender.get_menu_message()
    await call.message.edit_text(text=mailing_info[0], reply_markup=mailing_info[1], disable_web_page_preview=True)

@mailing_router.callback_query(IsAdmin(), F.data==MD.Menu.media)
async def start_update_media(call: types.CallbackQuery, state: FSMContext):
    message = await call.message.edit_text(text=MT.mailing_media, reply_markup=await MK.back_to_mailing_keyboard())
    await state.update_data(message_id=message.message_id)
    await state.set_state(MailingState.media)

@mailing_router.message(IsAdmin(), MailingState.media, F.content_type.in_([CT.AUDIO, CT.VIDEO, CT.VOICE, 
                                                                CT.ANIMATION, CT.PHOTO, CT.DOCUMENT, 
                                                                CT.VIDEO_NOTE]))
async def update_media(message: types.Message, state: FSMContext):
    await message.delete()
    
    types = {
        CT.AUDIO: (CT.AUDIO, message.audio.file_id if message.audio else None),
        CT.VIDEO: (CT.VIDEO, message.video.file_id if message.video else None),
        CT.VOICE: (CT.VOICE, message.voice.file_id if message.voice else None),
        CT.ANIMATION: (CT.ANIMATION, message.animation.file_id if message.animation else None),
        CT.PHOTO: (CT.PHOTO, message.photo[-1].file_id if message.photo else None),
        CT.DOCUMENT: (CT.DOCUMENT, message.document.file_id if message.document else None),
        CT.VIDEO_NOTE: (CT.VIDEO_NOTE, message.video_note.file_id if message.video_note else None)
    }

    content_type, media = types[message.content_type]
    
    await db.update(content_type=content_type, media=media)
    mailing_info = await sender.get_menu_message()
    message_id = (await state.get_data())['message_id']
    await message.bot.edit_message_text(chat_id=message.chat.id, message_id=message_id, text=mailing_info[0], reply_markup=mailing_info[1], disable_web_page_preview=True)
    await state.clear()

@mailing_router.callback_query(IsAdmin(), F.data==MD.Menu.text)
async def await_update_text(call: types.CallbackQuery, state: FSMContext):
    message = await call.message.edit_text(text=MT.mailing_text, reply_markup=await MK.back_to_mailing_keyboard(), disable_web_page_preview=True)
    await state.update_data(message_id=message.message_id)
    await state.set_state(MailingState.text)

@mailing_router.message(IsAdmin(), MailingState.text)
async def update_text(message: types.Message, state: FSMContext):
    await message.delete()
    await db.update(text=message.html_text)
    mailing_info = await sender.get_menu_message()
    message_id = (await state.get_data())['message_id']
    await message.bot.edit_message_text(chat_id=message.chat.id, message_id=message_id, text=mailing_info[0], reply_markup=mailing_info[1], disable_web_page_preview=True)
    await state.clear()

@mailing_router.callback_query(IsAdmin(), F.data==MD.Menu.button)
async def edit_button_menu(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text(text=MT.mailing_button_menu, reply_markup=await MK.mailing_button_edit_keyboard(), disable_web_page_preview=True)
    await state.update_data(message_id=call.message.message_id)

@mailing_router.callback_query(IsAdmin(), F.data.in_([MD.EditButton.button_link, MD.EditButton.button_text]))
async def await_update_button(call: types.CallbackQuery, state: FSMContext):
    
    types = {
        MD.EditButton.button_link: (MailingState.button_link, MT.mailing_button_link),
        MD.EditButton.button_text: (MailingState.button_text, MT.mailing_button_text)
    }

    await call.message.edit_text(text=types[call.data][1], reply_markup=await MK.back_to_mailing_keyboard(), disable_web_page_preview=True)
    await state.update_data(button=call.data)
    await state.set_state(types[call.data][0])

@mailing_router.message(IsAdmin(), MailingState.button_link, F.content_type.in_(CT.TEXT), F.text.regexp(r'https?://([a-zA-Z0-9.-]+)\.([a-zA-Z]{2,})\S*'))
async def update_button_link(message: types.Message, state: FSMContext):
    await message.delete()
    await db.update(button_link=message.text)
    mailing_info = await sender.get_menu_message()
    message_id = (await state.get_data())['message_id']
    await message.bot.edit_message_text(chat_id=message.chat.id, message_id=message_id, text=mailing_info[0], reply_markup=mailing_info[1], disable_web_page_preview=True)
    await state.clear()

@mailing_router.message(IsAdmin(), MailingState.button_text, F.content_type.in_(CT.TEXT))
async def update_button_text(message: types.Message, state: FSMContext):
    await message.delete()
    await db.update(button_text=message.text)
    mailing_info = await sender.get_menu_message()
    message_id = (await state.get_data())['message_id']
    await message.bot.edit_message_text(chat_id=message.chat.id, message_id=message_id, text=mailing_info[0], reply_markup=mailing_info[1], disable_web_page_preview=True)
    await state.clear()

@mailing_router.callback_query(IsAdmin(), F.data==MD.Menu.view_message)
async def preview_mailing(call: types.CallbackQuery, state: FSMContext):
    mailing_info = await db.get_mailing()
    content_type = await db.get_content_type()
    if content_type == 'text' and mailing_info.text == 'Не установлен':
        await call.answer(MT.mailing_not_set, show_alert=True)
    else:
        await sender.send_mailing_message(call.message.chat.id, mailing_info, content_type)

@mailing_router.callback_query(IsAdmin(), F.data==MD.Menu.start)
async def get_ready_to_start(call: types.CallbackQuery, state: FSMContext):
    users_count = await Config.UserDB.DB_INSTANCE.get_users_count()
    await call.message.edit_text(MT.mailing_sure.format(users_count), reply_markup=await MK.mailing_sure_keyboard(), disable_web_page_preview=True)

@mailing_router.callback_query(IsAdmin(), F.data==MD.StartMailing.sure)
async def mailing(call: types.CallbackQuery, state: FSMContext):
    users = await Config.UserDB.DB_INSTANCE.get_users_list()
    mailing_info = await db.get_mailing()
    content_type = await db.get_content_type()
    if content_type == 'text' and mailing_info.text == 'Не установлен':
        await call.answer(MT.mailing_not_set, show_alert=True)
        return
    await call.message.edit_text(MT.mailing_start.format(0, 0))
    result = await sender.mailing(mailing_info=mailing_info,
                                  content_type=content_type,
                                  users=users,
                                  chat_id=call.message.chat.id,
                                  message_id=call.message.message_id)
    await db.update(alive_users=result[0], died_users=result[1])
    await call.message.edit_text(MT.mailing_end.format(result[0], result[1]), reply_markup=await MK.back_to_mailing_keyboard())