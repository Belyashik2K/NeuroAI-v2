import base64

from aiogram import Router, F, types
from aiogram.filters.command import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.enums import ParseMode

from database import database as db
from database.models import User
from texts import UT, RB, IB, ET
from keyboards import inline, reply
from initialization import bot
from config import Config
from fsm import *
from neuros import neuro
from imageban import imageban
from filters import isNeuroActive

user_router = Router(name=__name__)

@user_router.message(CommandStart())
async def start(message: types.Message, user: User, state: FSMContext):
    await state.clear()
    data = [
        message.from_user.mention_html(),
        (await bot.get_me()).mention_html(),
        Config.technical_support,
        Config.ads
        ]
    await message.answer(UT.start_command.format(*data), reply_markup=await reply.get_start_keyboard(user=user), disable_web_page_preview=True)

@user_router.callback_query(F.data==IB.Callback.close)
async def close(call: types.CallbackQuery, user: User, state: FSMContext):
    await state.clear()
    await call.message.delete()

@user_router.message(F.text==RB.about)
async def about_us(message: types.Message, user: User, state: FSMContext):
    await state.clear()
    await message.answer(UT.AboutUs.about_us.format(**await db.get_neuro_statuses()), reply_markup=await inline.get_about_keyboard())

@user_router.message(F.text==RB.stats)
async def stats(message: types.Message, user: User, state: FSMContext):
    await state.clear()
    await message.answer(UT.Stats.stats.format(*await db.get_stats()), reply_markup=await inline.get_close_keyboard())

@user_router.message(F.text==RB.my_account)
async def profile(message: types.Message, user: User, state: FSMContext):
    await state.clear()
    data = [
        message.from_user.mention_html(),
        user.id,
        user.request_counter,
        user.registered_at.strftime('%d.%m.%Y %H:%M:%S'),
        ]
    await message.answer(UT.Profile.user.format(*data), reply_markup=await inline.get_close_keyboard())

@user_router.message(F.text==RB.neuro_choose)
async def neuro_category_choose(message: types.Message, user: User, state: FSMContext):
    await state.clear()
    await message.answer(UT.Neuros.choose_neuro_category, reply_markup=await inline.choose_category_keyboard())

@user_router.callback_query(F.data == IB.Callback.NeuroCategories.back)
async def neuro_category_choose_callback(call: types.CallbackQuery, user: User, state: FSMContext):
    await state.clear()
    await call.message.edit_text(UT.Neuros.choose_neuro_category, reply_markup=await inline.choose_category_keyboard())

@user_router.callback_query(F.data.startswith(IB.Callback.NeuroCategories.start))
async def neuro_choose(call: types.CallbackQuery, user: User, state: FSMContext):
    await call.message.edit_text(UT.Neuros.choose_neuro + getattr(UT.Neuros, call.data), reply_markup=await inline.choose_neuro_keyboard(category=call.data))
    await state.update_data(category=call.data)

@user_router.callback_query(F.data == IB.Callback.Mode.one_request)
async def one_request_mode(call: types.CallbackQuery, user: User, state: FSMContext):
    data = await state.get_data()
    neuro = getattr(IB.Neuros, data['neuro'].split('_')[1])
    mode = getattr(IB.Mode, call.data.split('_', 1)[1])
    await call.message.edit_text(UT.Neuros.one_request_mode.format(neuro, mode), reply_markup=await inline.get_back_keyboard(data['neuro']))
    await state.update_data(mode=call.data, message_id=call.message.message_id)
    await state.set_state(NeuroRequest.request)

@user_router.message(NeuroRequest.request, F.text)
async def one_request(message: types.Message, user: User, state: FSMContext):
    data = await state.get_data()
    formatting = [
        getattr(IB.Neuros, data['neuro'].split('_')[1]),
        getattr(IB.Mode, data['mode'].split('_', 1)[1]),
        message.text
        ]
    await message.delete()
    await bot.edit_message_text(UT.Neuros.one_request_processing.format(*formatting), chat_id=message.chat.id, message_id=data['message_id'])
    await state.clear()
    result = await neuro.text_neuro(neuro=data['neuro'], message=message.text, mode=data['mode'])
    formatting.append(result[0])
    try:
        await bot.edit_message_text(UT.Neuros.one_request_result.format(*formatting), chat_id=message.chat.id, message_id=data['message_id'], reply_markup=await inline.get_back_keyboard(data['neuro']), parse_mode=ParseMode.MARKDOWN)
    except Exception as e:
        if "end of the entity starting" in str(e):
            try:
                await message.bot.edit_message_text(chat_id=message.chat.id, message_id=data['message_id'], text=UT.Neuros.answer.format(result[0]), parse_mode=ParseMode.HTML)
            except:
                await message.bot.edit_message_text(chat_id=message.chat.id, message_id=data['message_id'], text=ET.error_with_entities)
        elif "MESSAGE_TOO_LONG" in str(e):
            await bot.edit_message_text(chat_id=message.chat.id, message_id=data['message_id'], text=ET.error_with_lenght)
        else:
            await bot.edit_message_text(chat_id=message.chat.id, message_id=data['message_id'], text=ET.unknown_error)
    await db.update_user(user_id=user.user_id, request_counter=user.request_counter + 1)

@user_router.callback_query(F.data==IB.Callback.Mode.chat)
async def chat_mode(call: types.CallbackQuery, user: User, state: FSMContext):
    await call.message.delete()
    data = await state.get_data()
    neuro_ = getattr(IB.Neuros, data['neuro'].split('_')[1])
    mode = getattr(IB.Mode, call.data.split('_', 1)[1])
    m = await bot.send_message(call.message.chat.id, UT.Neuros.awaiting_chat_code)
    _, chat_code = await neuro.text_neuro(neuro=data['neuro'], message="Hello!", mode=IB.Callback.Mode.one_request)
    await bot.delete_message(call.message.chat.id, m.message_id)
    await bot.send_message(call.message.chat.id, UT.Neuros.chat_mode.format(neuro_, mode), reply_markup=await reply.stop_chatting_keyboard())
    await state.update_data(mode=call.data, chat_code=chat_code)
    await state.set_state(NeuroRequest.chating)

@user_router.message(NeuroRequest.chating)
async def chatting(message: types.Message, user: User, state: FSMContext):
    data = await state.get_data()
    text = message.text
    if text != RB.stop_chatting:
        m = await bot.send_message(message.chat.id, UT.Neuros.chatting, parse_mode=ParseMode.MARKDOWN)
        if message.photo:
            text = message.caption or UT.Neuros.what_on_image
            photo = await bot.get_file(message.photo[-1].file_id)
            url = "https://api.telegram.org/file/bot{}/{}".format(Config.BOT_TOKEN, photo.file_path)
            text += UT.Neuros.image_link.format(await imageban.upload_image(url))
        result = await neuro.text_neuro(neuro=data['neuro'], message=text, mode=data['mode'], chat_code=data['chat_code'])
        try:
            await message.bot.edit_message_text(chat_id=message.chat.id, message_id=m.message_id, text=UT.Neuros.answer.format(result[0]), parse_mode=ParseMode.MARKDOWN)
            await state.set_state(NeuroRequest.chating)
            await db.update_user(user_id=user.user_id, request_counter=user.request_counter + 1)
        except Exception as e:
            if "end of the entity starting" in str(e):
                try:
                    await message.bot.edit_message_text(chat_id=message.chat.id, message_id=m.message_id, text=UT.Neuros.answer.format(result[0]), parse_mode=ParseMode.HTML)
                except:
                    await message.bot.edit_message_text(chat_id=message.chat.id, message_id=m.message_id, text=ET.error_with_entities)
            elif "MESSAGE_TOO_LONG" in str(e):
                await bot.edit_message_text(chat_id=message.chat.id, message_id=m.message_id, text=ET.error_with_lenght)
            else:
                await bot.edit_message_text(chat_id=message.chat.id, message_id=m.message_id, text=ET.unknown_error)
    else:
        await state.clear()
        await message.delete()
        await bot.send_message(message.chat.id, UT.Neuros.stop_chatting, reply_markup=await reply.get_start_keyboard(user=user))

@user_router.message(NeuroRequest.image_request, F.text)
async def image_request(message: types.Message, user: User, state: FSMContext):
    await message.delete()
    data = await state.get_data()
    neuro_ = getattr(IB.Neuros, data['neuro'].split('_')[1])
    await bot.edit_message_text(UT.Neuros.gen_image_processing.format(neuro_, message.text), chat_id=message.chat.id, message_id=data['message_id'])
    await state.clear()
    result = await neuro.image_neuro(neuro=data['neuro'], prompt=message.text)
    await bot.delete_message(message.chat.id, data['message_id'])
    await bot.send_photo(chat_id=message.chat.id, 
                         photo=types.BufferedInputFile(base64.b64decode(result), filename='photo.png'),
                         caption=UT.Neuros.gen_image_result.format(neuro_, message.text),
                         reply_markup=await inline.get_close_keyboard(),
                         parse_mode=ParseMode.MARKDOWN)
    await db.update_user(user_id=user.user_id, request_counter=user.request_counter + 1)

@user_router.callback_query(F.data.in_([IB.Callback.Neuros.gpt, IB.Callback.Neuros.claude, 
                                         IB.Callback.Neuros.google, IB.Callback.Neuros.llama, 
                                         IB.Callback.Neuros.gemini, IB.Callback.Neuros.mistral]), 
                                         isNeuroActive())
async def text_mode_choose(call: types.CallbackQuery, user: User, state: FSMContext):
    await state.clear()
    await call.message.edit_text(UT.Neuros.choose_mode.format(getattr(IB.Neuros, call.data.split('_')[1])), reply_markup=await inline.choose_mode_keyboard())
    await state.update_data(neuro=call.data)

@user_router.callback_query(F.data.in_([IB.Callback.Neuros.stable, IB.Callback.Neuros.playground, 
                                        IB.Callback.Neuros.midjourney, IB.Callback.Neuros.dalle3]), 
                                        isNeuroActive())
async def start_gen_image(call: types.CallbackQuery, user: User, state: FSMContext):
    await call.message.edit_text(UT.Neuros.start_gen_image.format(getattr(IB.Neuros, call.data.split('_')[1])), reply_markup=await inline.get_back_keyboard(IB.Callback.NeuroCategories.image), disable_web_page_preview=True)
    await state.update_data(neuro=call.data, message_id=call.message.message_id)
    await state.set_state(NeuroRequest.image_request)

@user_router.callback_query(F.data==IB.Callback.StartMenu.choose_neuro)
async def neuro_category_choose(call: types.CallbackQuery, user: User, state: FSMContext):
    await state.clear()
    await call.message.edit_text(UT.Neuros.choose_neuro_category, reply_markup=await inline.choose_category_keyboard())

@user_router.callback_query(F.data==IB.Callback.StartMenu.my_account)
async def profile(call: types.CallbackQuery, user: User, state: FSMContext):
    await state.clear()
    data = [
        call.from_user.mention_html(),
        user.id,
        user.request_counter,
        user.registered_at.strftime('%d.%m.%Y %H:%M:%S'),
        ]
    await call.message.edit_text(UT.Profile.user.format(*data), reply_markup=await inline.get_close_keyboard())

@user_router.callback_query(F.data==IB.Callback.StartMenu.stats)
async def stats(call: types.CallbackQuery, user: User, state: FSMContext):
    await state.clear()
    await call.message.edit_text(UT.Stats.stats.format(*await db.get_stats()), reply_markup=await inline.get_close_keyboard())

@user_router.callback_query(F.data==IB.Callback.StartMenu.about)
async def about_us(call: types.CallbackQuery, user: User, state: FSMContext):
    await state.clear()
    await call.message.edit_text(UT.AboutUs.about_us.format(**await db.get_neuro_statuses()), reply_markup=await inline.get_about_keyboard())

@user_router.callback_query(F.data==IB.Callback.Neuros.enhance, isNeuroActive())
async def enhance_image(call: types.CallbackQuery, user: User, state: FSMContext):
    neuro_ = getattr(IB.Neuros, call.data.split('_')[1])
    await call.message.edit_text(UT.Neuros.enchance_image.format(neuro_), reply_markup=await inline.get_back_keyboard(IB.Callback.NeuroCategories.image))
    await state.update_data(neuro=call.data, message_id=call.message.message_id)
    await state.set_state(NeuroRequest.enchance_image)

@user_router.message(NeuroRequest.enchance_image, F.photo)
async def enchance_image(message: types.Message, user: User, state: FSMContext):
    data = await state.get_data()
    neuro_ = getattr(IB.Neuros, data['neuro'].split('_')[1])
    await message.delete()
    await bot.edit_message_text(UT.Neuros.enchance_image_processing.format(neuro_), chat_id=message.chat.id, message_id=data['message_id'])
    photo = await bot.get_file(message.photo[-1].file_id)
    url = "https://api.telegram.org/file/bot{}/{}".format(Config.BOT_TOKEN, photo.file_path)
    result = await neuro.enchance_image_neuro(neuro=data['neuro'], image=url)
    await bot.delete_message(message.chat.id, data['message_id'])
    await bot.send_photo(chat_id=message.chat.id, 
                         photo=types.BufferedInputFile(base64.b64decode(result), filename='photo.png'),
                         caption=UT.Neuros.enchance_image_result.format(neuro_),
                         reply_markup=await inline.get_close_keyboard(),
                         parse_mode=ParseMode.MARKDOWN)
    await db.update_user(user_id=user.user_id, request_counter=user.request_counter + 1)

@user_router.callback_query(F.data==IB.Callback.Neuros.sdv, isNeuroActive())
async def sdv_image(call: types.CallbackQuery, user: User, state: FSMContext):
    neuro_ = getattr(IB.Neuros, call.data.split('_')[1])
    await call.message.edit_text(UT.Neuros.sdv_video.format(neuro_), reply_markup=await inline.get_back_keyboard(IB.Callback.NeuroCategories.image))
    await state.update_data(neuro=call.data, message_id=call.message.message_id)
    await state.set_state(NeuroRequest.sdv)

@user_router.message(NeuroRequest.sdv, F.photo)
async def sdv_image(message: types.Message, user: User, state: FSMContext):
    data = await state.get_data()
    neuro_ = getattr(IB.Neuros, data['neuro'].split('_')[1])
    await message.delete()
    await bot.edit_message_text(UT.Neuros.sdv_video_processing.format(neuro_), chat_id=message.chat.id, message_id=data['message_id'])
    photo = await bot.get_file(message.photo[-1].file_id)
    url = "https://api.telegram.org/file/bot{}/{}".format(Config.BOT_TOKEN, photo.file_path)
    result = await neuro.sdv_neuro(neuro=data['neuro'], image_url=url)
    await bot.delete_message(message.chat.id, data['message_id'])
    await bot.send_video(chat_id=message.chat.id, 
                         video=types.URLInputFile(result, filename='video.mp4'),
                         caption=UT.Neuros.sdv_video_result.format(neuro_),
                         reply_markup=await inline.get_close_keyboard(),
                         parse_mode=ParseMode.MARKDOWN)
    await db.update_user(user_id=user.user_id, request_counter=user.request_counter + 1)

@user_router.callback_query(F.data==IB.Callback.Neuros.whisper, isNeuroActive())
async def whisper_voice(call: types.CallbackQuery, user: User, state: FSMContext):
    neuro_ = getattr(IB.Neuros, call.data.split('_')[1])
    await call.message.edit_text(UT.Neuros.whisper_voice.format(neuro_), reply_markup=await inline.get_back_keyboard(IB.Callback.NeuroCategories.audio))
    await state.update_data(neuro=call.data, message_id=call.message.message_id)
    await state.set_state(NeuroRequest.whisper)

@user_router.message(NeuroRequest.whisper, F.audio)
async def whisper_voice(message: types.Message, user: User, state: FSMContext):
    # TODO: add whisper voice processing
    data = await state.get_data()
    neuro_ = getattr(IB.Neuros, data['neuro'].split('_')[1])
    await message.delete()
    await bot.edit_message_text(UT.Neuros.whisper_voice_processing.format(neuro_), chat_id=message.chat.id, message_id=data['message_id'])
    audio = await bot.get_file(message.audio.file_id)
    url = "https://api.telegram.org/file/bot{}/{}".format(Config.BOT_TOKEN, audio.file_path)
    result = await neuro.whisper_neuro(neuro=data['neuro'], file=url)
    await bot.edit_message_text(chat_id=message.chat.id, message_id=data['message_id'], text=UT.Neuros.whisper_voice_result.format(neuro_, result), reply_markup=await inline.get_close_keyboard(), parse_mode=ParseMode.MARKDOWN)
    await db.update_user(user_id=user.user_id, request_counter=user.request_counter + 1)

@user_router.callback_query(F.data==IB.Callback.Neuros.bender, isNeuroActive())
async def bender_voice(call: types.CallbackQuery, user: User, state: FSMContext):
    neuro_ = getattr(IB.Neuros, call.data.split('_')[1])
    await call.message.edit_text(UT.Neuros.bender_voice.format(neuro_), reply_markup=await inline.get_back_keyboard(IB.Callback.NeuroCategories.audio))
    await state.update_data(neuro=call.data, message_id=call.message.message_id)
    await state.set_state(NeuroRequest.bender)

@user_router.message(NeuroRequest.bender, F.text)
async def bender_voice(message: types.Message, user: User, state: FSMContext):
    await message.delete()
    data = await state.get_data()
    await bot.edit_message_text(UT.Neuros.bender_voice_processing.format(getattr(IB.Neuros, data['neuro'].split('_')[1]), message.text[:330]), chat_id=message.chat.id, message_id=data['message_id'])
    r = await neuro.bender_neuro(data['neuro'], message.text)
    await bot.delete_message(message.chat.id, data['message_id'])
    await bot.send_audio(chat_id=message.chat.id, 
                         audio=types.BufferedInputFile(r, filename=f"result_{message.from_user.id}.mp3"), 
                         caption=UT.Neuros.bender_voice_result.format(getattr(IB.Neuros, data['neuro'].split('_')[1]), message.text[:330]), 
                         reply_markup=await inline.get_close_keyboard(),
                         parse_mode=ParseMode.MARKDOWN)
    await db.update_user(user_id=user.user_id, request_counter=user.request_counter + 1)
    await state.clear()

@user_router.message(F.text==RB.stop_chatting)
async def stop_chatting(message: types.Message, user: User, state: FSMContext):
    await state.clear()
    await message.delete()
    await message.answer(UT.Neuros.stop_chatting, reply_markup=await reply.get_start_keyboard(user=user))

@user_router.message(F.text)
async def unknown_command(message: types.Message, user: User, state: FSMContext):
    await state.clear()
    await message.answer(ET.unknown_command, reply_markup=await inline.get_start_keyboard())
