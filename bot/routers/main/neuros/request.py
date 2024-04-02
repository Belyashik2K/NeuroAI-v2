import logging
from typing import Final

from aiogram import Router, F, types
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.utils.chat_action import ChatActionSender
from aiogram_i18n import I18nContext, LazyProxy

from ....neuros import *
from ....enums import *
from ....fsm import *
from ....database import database
from ....database.models import User
from ....keyboards import inline, data, reply
from ....utils.check_exception import ExceptionChecker
from ....utils.links import Links
from ....utils.chatting import Chatting
from ....utils.text_helper import TextHelper

router: Final[Router] = Router(name=__name__)


@router.message(NeuroRequest.request, F.text)
async def one_request(message: types.Message, user: User, state: FSMContext, i18n: I18nContext):
    _data = await state.get_data()
    formatting = {
        "neuro": LazyProxy(f"buttons-{_data['neuro']}").data,
        "mode": LazyProxy(f"buttons-{_data['mode']}").data,
        "request": message.text
    }
    header = i18n.messages.header(neuro=formatting['neuro'], mode=formatting['mode'])
    await message.delete()
    m = await message.bot.edit_message_text(header + "\n\n" + i18n.messages.request_processing(**formatting),
                                            chat_id=message.chat.id, message_id=_data['message_id'])
    await state.clear()
    async with ChatActionSender.typing(bot=message.bot, chat_id=message.chat.id):
        if _data['provider'] == Provider.FUTUREFORGE:
            result = await future.text_neuro(neuro=_data['neuro'], message=message.text, mode=_data['mode'])
        else:
            result = await vision.chatting(neuro=_data['neuro'],
                                           messages=Chatting.prepare_messages(content=message.text,
                                                                              role=Role.USER,
                                                                              message_list=[],
                                                                              neuro=_data['neuro']))
        formatting['result'] = result[0]
        try:
            await message.bot.delete_message(chat_id=message.chat.id,
                                             message_id=m.message_id)
            await message.answer(header + "\n\n" + i18n.messages.request_result(**formatting) + result[0],
                                 reply_markup=await inline.close_or_again(_data['neuro']))
        except Exception as e:
            logging.error(e)
            await message.answer(**ExceptionChecker.check_exception(str(e)))
    await database.update_user(user_id=user.user_id,
                               request_counter=user.request_counter + 1)


@router.callback_query(data.Mode.filter(F.type_ == Mode.CHAT))
async def chat_mode(call: types.CallbackQuery, callback_data: data.Mode,
                    user: User, state: FSMContext, i18n: I18nContext):
    await call.message.delete()
    _data = await state.get_data()

    formatting = {
        "neuro": LazyProxy(f"buttons-{_data['neuro']}").data,
        "mode": LazyProxy(f"buttons-{callback_data.type_}").data,
    }
    header = i18n.messages.header(neuro=formatting['neuro'], mode=formatting['mode'])

    m = await call.bot.send_message(call.message.chat.id, i18n.messages.starting_chat())
    if _data['provider'] == Provider.FUTUREFORGE:
        _, chat_code = await future.text_neuro(neuro=_data['neuro'], message="Hello!", mode=Mode.ONE)
    else:
        chat_code = None
        await state.update_data(chat_cache=[])
    await call.bot.delete_message(call.message.chat.id, m.message_id)
    await call.bot.send_message(call.message.chat.id,
                                header + '\n\n' + i18n.messages.chat_mode(
                                    end_button=LazyProxy('buttons-stop_chatting').data),
                                reply_markup=reply.stop_chatting())
    await state.update_data(mode=callback_data.type_, chat_code=chat_code)
    await state.set_state(NeuroRequest.chating)


@router.message(NeuroRequest.chating, F.text | F.photo)
async def chatting(message: types.Message, user: User, state: FSMContext, i18n: I18nContext):
    _data = await state.get_data()

    
    if message.text == LazyProxy("buttons-stop_chatting").data:
        await state.clear()
        await message.delete()
        await message.bot.send_message(message.chat.id, i18n.messages.stop_chatting(),
                                       reply_markup=reply.menu(user=user))
        return
    
    text = message.text
    url = ""

    if message.photo and _data['neuro'] == Neuro.LLAVA:
        photo = await message.bot.get_file(message.photo[-1].file_id)
        text = message.caption if message.caption else "What is on the photo?"
        url = Links.get_file_url(photo.file_path)
    elif message.photo and _data['neuro'] != Neuro.LLAVA:
        names = {
            "neuro": LazyProxy(f"buttons-{_data['neuro']}").data,
            "llava": LazyProxy(f"buttons-{Neuro.LLAVA}").data
        }
        async with ChatActionSender.typing(bot=message.bot, chat_id=message.chat.id):
            await message.reply(i18n.errors.cant_view_photo(**names))
        await state.set_state(NeuroRequest.chating)
        return 

    m = await message.bot.send_message(message.chat.id, i18n.messages.in_work(), parse_mode=ParseMode.MARKDOWN)
    async with ChatActionSender.typing(bot=message.bot, chat_id=message.chat.id):
        if _data['provider'] == Provider.FUTUREFORGE:
            result = await future.text_neuro(neuro=_data['neuro'], message=text, mode=_data['mode'],
                                             chat_code=_data['chat_code'])
        else:
            messages = Chatting.prepare_messages(content=text,
                                                 role=Role.USER,
                                                 message_list=_data['chat_cache'],
                                                 neuro=_data['neuro'],
                                                 image_url=url)
            result = await vision.chatting(neuro=_data['neuro'],
                                           messages=messages)
        await message.bot.delete_message(chat_id=message.chat.id, message_id=m.message_id)
        try:
            await message.reply(text=i18n.messages.chat_answer() + " " + result[0],
                                parse_mode=ParseMode.MARKDOWN)
            if _data['provider'] == Provider.VISIONCRAFT:
                with_assistant = Chatting.prepare_messages(content=result[0],
                                                           role=Role.ASSISTANT,
                                                           message_list=messages,
                                                           neuro=_data['neuro'],)
                await state.update_data(chat_cache=with_assistant)
        except Exception:
            try:
                await message.reply(text=i18n.messages.chat_answer() + " " + result[0],
                                    parse_mode=ParseMode.HTML)
            except Exception as e:
                logging.error(e)
                await message.reply(**ExceptionChecker.check_exception(str(e)))
    await state.set_state(NeuroRequest.chating)
    await database.update_user(user_id=user.user_id, request_counter=user.request_counter + 1)


@router.message(NeuroRequest.image_request, F.text | F.photo)
async def image_request(message: types.Message, user: User, state: FSMContext, i18n: I18nContext):
    await message.delete()
    _data = await state.get_data()

    if _data['neuro'] != Neuro.VIDEODIFFUSION and message.photo:
        return

    formatting = {
        'neuro': LazyProxy(f"buttons-{_data['neuro']}").data,
    }

    neuros = {
        Neuro.VIDEODIFFUSION: future.sdv_neuro,
    }

    if _data['neuro'] in neuros:
        photo = await message.bot.get_file(message.photo[-1].file_id)
        prompt = Links.get_file_url(photo.file_path)
        text = i18n.messages.other_processing(neuro=formatting['neuro'])
        func = neuros[_data['neuro']]
    else:
        prompt = TextHelper.prepaire_text(message.text)
        text = i18n.messages.image_processing(neuro=formatting['neuro'], prompt=prompt)
        func = future.image_neuro if _data['provider'] == Provider.FUTUREFORGE else vision.image_neuro
    formatting['prompt'] = prompt

    await message.bot.edit_message_text(text, chat_id=message.chat.id, message_id=_data['message_id'])
    await state.clear()
    result = await func(_data['neuro'], prompt)
    await message.bot.delete_message(message.chat.id, _data['message_id'])
    if type(result) in [str, bytes]:
        temp = result if type(result) == str else 'bytes'
        if not temp.endswith(".mp4"):
            async with ChatActionSender.upload_photo(bot=message.bot, chat_id=message.chat.id):
                photo_obj = types.URLInputFile(result, filename='photo.png') if type(result) == str else types.BufferedInputFile(result, filename='photo.png')
                await message.bot.send_photo(chat_id=message.chat.id,
                                             photo=photo_obj,
                                             caption=i18n.messages.image_result(**formatting),
                                             reply_markup=await inline.close_or_again(_data['neuro']),
                                             parse_mode=ParseMode.MARKDOWN)
        else:
            async with ChatActionSender.upload_video(bot=message.bot, chat_id=message.chat.id):
                await message.bot.send_video(chat_id=message.chat.id,
                                             video=types.URLInputFile(result, filename='video.mp4'),
                                             caption=i18n.messages.other_result(**formatting),
                                             reply_markup=await inline.close_or_again(_data['neuro']))
        await database.update_user(user_id=user.user_id, request_counter=user.request_counter + 1)
    else:
        async with ChatActionSender.upload_photo(bot=message.bot, chat_id=message.chat.id):
            photos = list()
            for url in result:
                photos.append(types.InputMediaPhoto(media=types.URLInputFile(url, filename='photo.png')))
            m = await message.bot.send_media_group(chat_id=message.chat.id,
                                                   media=photos)
            await message.answer(reply_to_message_id=m[-1].message_id,
                                 text=i18n.messages.image_result(**formatting),
                                 reply_markup=await inline.close_or_again(_data['neuro']),
                                 parse_mode=ParseMode.MARKDOWN)
        await database.update_user(user_id=user.user_id, request_counter=user.request_counter + 4)


@router.message(NeuroRequest.enchance_image, F.photo)
async def enchance_image(message: types.Message, user: User, state: FSMContext, i18n: I18nContext):
    await message.delete()
    _data = await state.get_data()

    formatting = {
        "neuro": LazyProxy(f"buttons-{_data['neuro']}").data,
    }

    await message.bot.edit_message_text(i18n.messages.other_processing(**formatting),
                                        chat_id=message.chat.id,
                                        message_id=_data['message_id'])
    photo = await message.bot.get_file(message.photo[-1].file_id)
    url = Links.get_file_url(photo.file_path)
    image = await vision.enchance_image(neuro=_data['neuro'],
                                        photo_url=url)
    await message.bot.delete_message(message.chat.id, _data['message_id'])
    async with ChatActionSender.upload_document(bot=message.bot, chat_id=message.chat.id):
        await message.bot.send_document(chat_id=message.chat.id,
                                        document=types.BufferedInputFile(image, filename='photo.png'),
                                        caption=i18n.messages.other_result(**formatting),
                                        reply_markup=await inline.close_or_again(_data['neuro']))
    await database.update_user(user_id=user.user_id, request_counter=user.request_counter + 1)
    await state.clear()


@router.message(NeuroRequest.bender, F.text)
async def bender_request(message: types.Message, user: User, state: FSMContext, i18n: I18nContext):
    await message.delete()
    data = await state.get_data()

    formatting = {
        "neuro": LazyProxy(f"buttons-{data['neuro']}").data,
        'prompt': message.text[:330]
    }

    await message.bot.edit_message_text(i18n.messages.image_processing(**formatting),
                                        chat_id=message.chat.id,
                                        message_id=data['message_id'])
    r = await future.bender_neuro(data['neuro'], message.text)
    await message.bot.delete_message(message.chat.id, data['message_id'])
    await message.bot.send_audio(chat_id=message.chat.id,
                                 audio=types.BufferedInputFile(r, filename=f"result_{message.from_user.id}.mp3"),
                                 caption=i18n.messages.image_result(**formatting),
                                 reply_markup=inline.close(),
                                 parse_mode=ParseMode.MARKDOWN)
    await database.update_user(user_id=user.user_id, request_counter=user.request_counter + 1)
    await state.clear()


@router.message(NeuroRequest.whisper, F.voice | F.audio)
async def whisper_voice(message: types.Message, user: User, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()
    file = message.voice or message.audio
    formatting = {
        "neuro": LazyProxy(f"buttons-{data['neuro']}").data,
        "mode": LazyProxy(f"buttons-{data['w_mode']}").data,
    }
    
    await message.delete()
    await message.bot.edit_message_text(i18n.messages.whisper_processing(**formatting),
                                        chat_id=message.chat.id,
                                        message_id=data['message_id'])
    audio = await message.bot.get_file(file.file_id)
    url = Links.get_file_url(audio.file_path)
    result = await vision.whisper(audio=url, task=data['w_mode'])
    formatting['result'] = result.strip()
    await message.bot.edit_message_text(chat_id=message.chat.id,
                                        message_id=data['message_id'],
                                        text=i18n.messages.whisper_result(**formatting),
                                        reply_markup=await inline.close_or_again(data['neuro']))
    await database.update_user(user_id=user.user_id, request_counter=user.request_counter + 1)


@router.message(NeuroRequest.tencentmaker, F.photo & F.caption)
async def tencentmaker(message: types.Message, user: User, state: FSMContext, i18n: I18nContext):
    await message.delete()
    data = await state.get_data()
    formatting = {
        "neuro": LazyProxy(f"buttons-{data['neuro']}").data,
        'prompt': message.caption
    }
    await message.bot.edit_message_text(i18n.messages.image_processing(**formatting),
                                        chat_id=message.chat.id,
                                        message_id=data['message_id'])
    photo = await message.bot.get_file(message.photo[-1].file_id)
    url = Links.get_file_url(photo.file_path)
    result = await future.tencentmaker(image_url=url, prompt=message.caption)
    await message.bot.delete_message(message.chat.id, data['message_id'])
    async with ChatActionSender.upload_photo(bot=message.bot, chat_id=message.chat.id):
        await message.bot.send_photo(chat_id=message.chat.id,
                                     photo=types.URLInputFile(result, filename='photo.png'),
                                     caption=i18n.messages.image_result(**formatting),
                                     reply_markup=await inline.close_or_again(data['neuro']),
                                     parse_mode=ParseMode.MARKDOWN)
    await database.update_user(user_id=user.user_id, request_counter=user.request_counter + 1)
    await state.clear()


@router.message(NeuroRequest.midjourneyv6, F.text)
async def midjourneyv6(message: types.Message, user: User, state: FSMContext, i18n: I18nContext):
    await message.delete()
    data = await state.get_data()
    formatting = {
        "neuro": LazyProxy(f"buttons-{data['neuro']}").data,
        'prompt': message.text
    }
    await message.bot.edit_message_text(i18n.messages.image_processing(**formatting),
                                        chat_id=message.chat.id,
                                        message_id=data['message_id'])
    result = await future.midjourneyv6(message.text)
    await message.bot.delete_message(message.chat.id, data['message_id'])

    photos = list()

    for url in result:
        photos.append(types.InputMediaPhoto(media=types.URLInputFile(url, filename='photo.png')))

    async with ChatActionSender.upload_photo(bot=message.bot, chat_id=message.chat.id):
        m = await message.bot.send_media_group(chat_id=message.chat.id,
                                               media=photos)
    await message.answer(reply_to_message_id=m[-1].message_id,
                         text=i18n.messages.image_result(**formatting),
                         reply_markup=await inline.close_or_again(data['neuro']),
                         parse_mode=ParseMode.MARKDOWN)
    await database.update_user(user_id=user.user_id,
                               request_counter=user.request_counter + 1)
    await state.clear()

@router.message(NeuroRequest.t2g, F.text)
async def t2g(message: types.Message, user: User, state: FSMContext, i18n: I18nContext):
    await message.delete()
    data = await state.get_data()
    formatting = {
        "neuro": LazyProxy(f"buttons-{data['neuro']}").data,
        'prompt': message.text
    }
    await message.bot.edit_message_text(i18n.messages.image_processing(**formatting),
                                        chat_id=message.chat.id,
                                        message_id=data['message_id'])
    result = await vision.text2gif(message.text)
    await message.bot.delete_message(message.chat.id, data['message_id'])
    async with ChatActionSender.upload_video(bot=message.bot, chat_id=message.chat.id):
        await message.bot.send_animation(chat_id=message.chat.id,
                                     animation=types.URLInputFile(result, filename='file.gif'),
                                     caption=i18n.messages.image_result(**formatting),
                                     reply_markup=await inline.close_or_again(data['neuro']),
                                     parse_mode=ParseMode.MARKDOWN)
    await database.update_user(user_id=user.user_id, request_counter=user.request_counter + 1)
    await state.clear()
    
@router.message(NeuroRequest.i2i, F.photo & F.caption)
async def i2i(message: types.Message, user: User, state: FSMContext, i18n: I18nContext):
    await message.delete()
    data = await state.get_data()
    formatting = {
        "neuro": LazyProxy(f"buttons-{data['neuro']}").data,
        'prompt': message.caption
    }
    await message.bot.edit_message_text(i18n.messages.image_processing(**formatting),
                                        chat_id=message.chat.id,
                                        message_id=data['message_id'])
    photo = await message.bot.get_file(message.photo[-1].file_id)
    url = Links.get_file_url(photo.file_path)
    result = await vision.image2image(image_url=url, prompt=message.caption)
    await message.bot.delete_message(message.chat.id, data['message_id'])
    async with ChatActionSender.upload_photo(bot=message.bot, chat_id=message.chat.id):
        await message.bot.send_photo(chat_id=message.chat.id,
                                     photo=types.BufferedInputFile(result, filename='photo.png'),
                                     caption=i18n.messages.image_result(**formatting),
                                     reply_markup=await inline.close_or_again(data['neuro']),
                                     parse_mode=ParseMode.MARKDOWN)
    await database.update_user(user_id=user.user_id, request_counter=user.request_counter + 1)
    await state.clear()
