import logging
from typing import Final

from aiogram import Router, F, types
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.utils.chat_action import ChatActionSender
from aiogram_i18n import I18nContext, LazyProxy

from ....database import database
from ....database.models import User
from ....keyboards import inline, data, reply
from ....neuros import client
from ....utils.check_exception import ExceptionChecker
from ....utils.links import Links

from ....fsm import *

router: Final[Router] = Router(name=__name__)

@router.message(NeuroRequest.request, F.text)
async def one_request(message: types.Message, user: User, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()
    formatting = {
        "neuro": LazyProxy(f"buttons-{data['neuro'].split('_')[1]}").data,
        "mode": LazyProxy(f"buttons-{data['mode'].split('_', 1)[1]}").data,
        "request": message.text
    }
    header = i18n.messages.header(neuro=formatting['neuro'], mode=formatting['mode'])
    await message.delete()
    m = await message.bot.edit_message_text(header + "\n\n" + i18n.messages.request_processing(**formatting),
                                        chat_id=message.chat.id, message_id=data['message_id'])
    await state.clear()
    async with ChatActionSender.typing(bot=message.bot, chat_id=message.chat.id):
        result = await client.text_neuro(neuro=data['neuro'], message=message.text, mode=data['mode'])
        formatting['result'] = result[0]
        try:
            await message.bot.delete_message(chat_id=message.chat.id,
                                            message_id=m.message_id)
            await message.answer(header + "\n\n" + i18n.messages.request_result(**formatting) + result[0],
                                reply_markup=inline.back(data['neuro']))
        except Exception as e:
            logging.error(e)
            await message.answer(**ExceptionChecker.check_exception(str(e)))
    await database.update_user(user_id=user.user_id,
                               request_counter=user.request_counter + 1)

@router.callback_query(F.data == data.Mode.chat)
async def chat_mode(call: types.CallbackQuery, user: User, state: FSMContext, i18n: I18nContext):
    await call.message.delete()
    _data = await state.get_data()

    formatting = {
        "neuro": LazyProxy(f"buttons-{_data['neuro'].split('_')[1]}").data,
        "mode": LazyProxy(f"buttons-{call.data.split('_', 1)[1]}").data,
    }
    header = i18n.messages.header(neuro=formatting['neuro'], mode=formatting['mode'])

    m = await call.bot.send_message(call.message.chat.id, i18n.messages.starting_chat())
    _, chat_code = await client.text_neuro(neuro=_data['neuro'], message="Hello!", mode=data.Mode.one_request)
    await call.bot.delete_message(call.message.chat.id, m.message_id)
    await call.bot.send_message(call.message.chat.id, 
                                header + '\n\n' + i18n.messages.chat_mode(end_button=LazyProxy('buttons-stop_chatting').data), 
                                reply_markup=reply.stop_chatting())
    await state.update_data(mode=call.data, chat_code=chat_code)
    await state.set_state(NeuroRequest.chating)

@router.message(NeuroRequest.chating, F.text)
async def chatting(message: types.Message, user: User, state: FSMContext, i18n: I18nContext):
    if message.text == LazyProxy("buttons-stop_chatting").data:
        await state.clear()
        await message.delete()
        await message.bot.send_message(message.chat.id, i18n.messages.stop_chatting(),
                                       reply_markup=reply.menu(user=user))
        return

    data = await state.get_data()
    text = message.text
    m = await message.bot.send_message(message.chat.id, i18n.messages.in_work(), parse_mode=ParseMode.MARKDOWN)
    async with ChatActionSender.typing(bot=message.bot, chat_id=message.chat.id):
        result = await client.text_neuro(neuro=data['neuro'], message=text, mode=data['mode'], chat_code=data['chat_code'])
        await message.bot.delete_message(chat_id=message.chat.id, message_id=m.message_id)
        try:
            await message.reply(text=i18n.messages.chat_answer() + " " + result[0],
                                parse_mode=ParseMode.MARKDOWN)
        except Exception as e:
            logging.error(e)
            await message.reply(**ExceptionChecker.check_exception(str(e)))
    await state.set_state(NeuroRequest.chating)
    await database.update_user(user_id=user.user_id, request_counter=user.request_counter + 1)

@router.message(NeuroRequest.image_request, F.text | F.photo)
async def image_request(message: types.Message, user: User, state: FSMContext, i18n: I18nContext):
    await message.delete()
    _data = await state.get_data()

    if _data['neuro'] not in [data.Neuros.sdv, data.Neuros.enhance] and message.photo:
        return

    formatting = {
        'neuro': LazyProxy(f"buttons-{_data['neuro'].split('_')[1]}").data,
    }

    neuros = {
        data.Neuros.sdv: client.sdv_neuro,
        data.Neuros.enhance: client.enchance_image_neuro,
    }

    if _data['neuro'] in neuros:
        photo = await message.bot.get_file(message.photo[-1].file_id)
        prompt = Links.get_file_url(photo.file_path)
        text = i18n.messages.other_processing(neuro=formatting['neuro'])
        func = neuros[_data['neuro']]
    else:
        prompt = message.text
        text = i18n.messages.image_processing(neuro=formatting['neuro'], prompt=prompt)
        func = client.image_neuro
    formatting['prompt'] = prompt

    await message.bot.edit_message_text(text, chat_id=message.chat.id, message_id=_data['message_id'])
    await state.clear()
    result = await func(_data['neuro'], prompt)
    await message.bot.delete_message(message.chat.id, _data['message_id'])

    if not result.endswith(".mp4"):
        async with ChatActionSender.upload_photo(bot=message.bot, chat_id=message.chat.id):
            await message.bot.send_photo(chat_id=message.chat.id,
                                        photo=types.URLInputFile(result, filename='photo.png'),
                                        caption=i18n.messages.image_result(**formatting),
                                        reply_markup=inline.close(),
                                        parse_mode=ParseMode.MARKDOWN)
    else:
        async with ChatActionSender.upload_video(bot=message.bot, chat_id=message.chat.id):
            await message.bot.send_video(chat_id=message.chat.id,
                                        video=types.URLInputFile(result, filename='video.mp4'),
                                        caption=i18n.messages.other_result(**formatting),
                                        reply_markup=inline.close())

    await database.update_user(user_id=user.user_id, request_counter=user.request_counter + 1)

@router.message(NeuroRequest.bender, F.text)
async def bender_request(message: types.Message, user: User, state: FSMContext, i18n: I18nContext):
    await message.delete()
    data = await state.get_data()

    formatting = {
        "neuro": LazyProxy(f"buttons-{data['neuro'].split('_')[1]}").data,
        'prompt': message.text[:330]
    }

    await message.bot.edit_message_text(i18n.messages.image_processing(**formatting),
                                        chat_id=message.chat.id,
                                        message_id=data['message_id'])
    r = await client.bender_neuro(data['neuro'], message.text)
    await message.bot.delete_message(message.chat.id, data['message_id'])
    await message.bot.send_audio(chat_id=message.chat.id,
                                 audio=types.BufferedInputFile(r, filename=f"result_{message.from_user.id}.mp3"),
                                 caption=i18n.messages.image_result(**formatting),
                                 reply_markup=inline.close(),
                                 parse_mode=ParseMode.MARKDOWN)
    await database.update_user(user_id=user.user_id, request_counter=user.request_counter + 1)
    await state.clear()

@router.message(NeuroRequest.whisper, F.audio)
async def whisper_voice(message: types.Message, user: User, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()
    formatting = {
        "neuro": LazyProxy(f"buttons-{data['neuro'].split('_')[1]}").data,
    }
    await message.delete()
    await message.bot.edit_message_text(i18n.messages.other_processing(**formatting),
                                        chat_id=message.chat.id,
                                        message_id=data['message_id'])
    audio = await message.bot.get_file(message.audio.file_id)
    url = Links.get_file_url(audio.file_path)
    result = await client.whisper_neuro(neuro=data['neuro'], file_url=url)
    await message.bot.edit_message_text(chat_id=message.chat.id,
                                        message_id=data['message_id'],
                                        text=i18n.messages.other_result(**formatting) + '\n\n' + i18n.messages.answer(
                                            result=result),
                                        reply_markup=inline.close())
    await database.update_user(user_id=user.user_id, request_counter=user.request_counter + 1)

@router.message(NeuroRequest.tencentmaker, F.photo & F.caption)
async def tencentmaker(message: types.Message, user: User, state: FSMContext, i18n: I18nContext):
    await message.delete()
    data = await state.get_data()
    formatting = {
        "neuro": LazyProxy(f"buttons-{data['neuro'].split('_')[1]}").data,
        'prompt': message.caption
    }
    await message.bot.edit_message_text(i18n.messages.image_processing(**formatting),
                                        chat_id=message.chat.id,
                                        message_id=data['message_id'])
    photo = await message.bot.get_file(message.photo[-1].file_id)
    url = Links.get_file_url(photo.file_path)
    result = await client.tencentmaker(image_url=url, prompt=message.caption)
    await message.bot.delete_message(message.chat.id, data['message_id'])
    async with ChatActionSender.upload_photo(bot=message.bot, chat_id=message.chat.id):
        await message.bot.send_photo(chat_id=message.chat.id,
                                    photo=types.URLInputFile(result, filename='photo.png'),
                                    caption=i18n.messages.image_result(**formatting),
                                    reply_markup=inline.close(),
                                    parse_mode=ParseMode.MARKDOWN)
    await database.update_user(user_id=user.user_id, request_counter=user.request_counter + 1)
    await state.clear()

@router.message(NeuroRequest.midjourneyv6, F.text)
async def midjourneyv6(message: types.Message, user: User, state: FSMContext, i18n: I18nContext):
    await message.delete()
    data = await state.get_data()
    formatting = {
        "neuro": LazyProxy(f"buttons-{data['neuro'].split('_')[1]}").data,
        'prompt': message.text
    }
    await message.bot.edit_message_text(i18n.messages.image_processing(**formatting),
                                        chat_id=message.chat.id,
                                        message_id=data['message_id'])
    result = await client.midjourneyv6(message.text)
    await message.bot.delete_message(message.chat.id, data['message_id'])
    
    photos = list()

    for url in result:
        photos.append(types.InputMediaPhoto(media=types.URLInputFile(url, filename='photo.png')))

    async with ChatActionSender.upload_photo(bot=message.bot, chat_id=message.chat.id):
        m = await message.bot.send_media_group(chat_id=message.chat.id,
                                                media=photos)
    await message.answer(reply_to_message_id=m[-1].message_id,
                        text=i18n.messages.image_result(**formatting),
                        reply_markup=inline.close(),
                        parse_mode=ParseMode.MARKDOWN)
    await database.update_user(user_id=user.user_id, 
                               request_counter=user.request_counter + 1)
    await state.clear()