from typing import Final

from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram_i18n import I18nContext

from ...database.models import User
from ...keyboards import inline

router: Final[Router] = Router(name=__name__)

@router.message()
async def unknown_command(message: Message, i18n: I18nContext, user: User, state: FSMContext):
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