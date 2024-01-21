from typing import Final

from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram_i18n import I18nContext, LazyProxy

from ...database.models import User
from ...keyboards import inline, reply

router: Final[Router] = Router(name=__name__)

@router.message()
async def unknown_command(message: Message, i18n: I18nContext, user: User, state: FSMContext):
    if message.text == LazyProxy("buttons-stop_chatting").data:
        await state.clear()
        await message.delete()
        await message.bot.send_message(message.chat.id, i18n.messages.stop_chatting(), reply_markup=reply.menu(user=user))
        return

    if user.first_language_set:
        await state.clear()
        await message.answer(
            i18n.errors.unknown_command(),
            reply_markup=inline.start()
        )
    else:
        await message.answer(
            i18n.messages.start(name=user.mention),
            reply_markup=inline._locales()
        )