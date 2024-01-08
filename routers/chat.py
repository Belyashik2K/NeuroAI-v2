from aiogram import F, Router, types
from aiogram.enums import ChatType as ChT
from aiogram.enums.content_type import ContentType as CT
from aiogram.filters.chat_member_updated import (ChatMemberUpdatedFilter, 
                                                 IS_NOT_MEMBER, 
                                                 MEMBER, 
                                                 ADMINISTRATOR)
from aiogram.filters.command import Command

from initialization import bot
from utils import Utils as U
from database import database
from database.models import Chat
from neuros import neuro
from texts import IB, CT as ChatTexts
from filters import IsUserAdminInChat
from keyboards import inline

chat_router = Router(name=__name__)
chat_router.message.filter(F.chat.type.in_([ChT.GROUP, ChT.SUPERGROUP]))

@chat_router.my_chat_member(
        ChatMemberUpdatedFilter(
        member_status_changed=IS_NOT_MEMBER >> (MEMBER | ADMINISTRATOR)
        ))
async def bot_added(event: types.ChatMemberUpdated):
    me = await bot.get_me()
    await event.answer(ChatTexts.added_to_chat.format(me.mention_html()), disable_web_page_preview=True)

@chat_router.message(F.voice) # | F.video_note when video_note will be supported
async def transcription_voice(message: types.Message, chat: Chat):
    file_type = message.voice 
    # if message.voice else message.video_note
    file = await bot.get_file(file_type.file_id)
    link = U.get_file_url(file.file_path)
    if chat.automatic_transcription:
        transcription = await neuro.whisper_neuro(IB.Callback.Neuros.whisper, link)
        await message.reply(ChatTexts.whisper_transcript.format(
            transcription, 
            (await message.bot.get_me()).mention_html())
            )
        await database.update_chat(chat.chat_id, request_counter=chat.request_counter + 1)

@chat_router.message(Command('neuroai'), IsUserAdminInChat())
async def settings(message: types.Message, chat: Chat):
    await message.answer(ChatTexts.neuroai.format(
        chat.id,
        chat.request_counter,
        ChatTexts.autotrans[chat.automatic_transcription]
        ), reply_markup=await inline.change_autotranscrip_keyboard(chat.automatic_transcription))
    
@chat_router.callback_query(F.data == IB.Callback.Chat.autotrans, IsUserAdminInChat())
async def switch_autotrans(call: types.CallbackQuery, chat: Chat):
    await call.answer()
    await database.update_chat(chat.chat_id, automatic_transcription=not chat.automatic_transcription)
    await call.message.edit_text(ChatTexts.neuroai.format(
        chat.id,
        chat.request_counter,
        ChatTexts.autotrans[not chat.automatic_transcription]
        ), reply_markup=await inline.change_autotranscrip_keyboard(not chat.automatic_transcription))