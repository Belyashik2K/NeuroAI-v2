from typing import Final

from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import any_state
from aiogram.filters.command import CommandStart
from aiogram_i18n import I18nContext

from ...database import database
from ...database.models import User
from ...keyboards import inline, reply
from ...enums import Locale
from ...config import config

router: Final[Router] = Router(name=__name__)

@router.message(any_state, CommandStart())
async def start(message: types.Message, user: User,  i18n: I18nContext, state: FSMContext):
    await state.clear()
    if not user.first_language_set:
        await message.answer(
            i18n.messages.start(name=user.mention),
            reply_markup=inline._locales()
        )
    else:
        formatting = {
            'name': message.from_user.mention_html(),
            'self': (await message.bot.get_me()).mention_html(),
            'technical_support': config.technical_support,
            'ads': config.ads
        }
        await message.answer(
            i18n.messages.info(**formatting),
            reply_markup=reply.menu(user)
        )

@router.callback_query(F.data.in_(Locale.DATA_LIST))
async def menu(call: types.CallbackQuery, user: User, i18n: I18nContext):
    if not user.first_language_set:
        await call.message.delete()
        await i18n.set_locale(call.data)
        await database.update_user(user.user_id, first_language_set=True)
        formatting = {
            'name': call.from_user.mention_html(),
            'self': (await call.bot.get_me()).mention_html(),
            'technical_support': config.technical_support,
            'ads': config.ads
        }
        await call.message.answer(
            i18n.messages.info(**formatting),
            reply_markup=reply.menu(user)
        )
    else:
        if user.locale == call.data:
            await call.answer(i18n.errors.lang_already_set())
            return
        await i18n.set_locale(call.data)
        await call.answer(i18n.messages.lang_set())
        await call.message.delete()
        await call.message.answer(
            i18n.messages.lang_set(),
            reply_markup=reply.menu(user)
        )