import logging

from typing import Final

from aiogram import F, Router
from aiogram.types import ErrorEvent
from aiogram_i18n import I18nContext

from ...database.models import User
from ...utils.notify import sender
from ...keyboards import inline

router: Final[Router] = Router(name=__name__)

@router.errors()
async def handle_some_error(error: ErrorEvent, i18n: I18nContext, user: User):
    logging.error(error.exception)
    await sender.error_notify(user_id=user.user_id,
                                mention=error.update.message.from_user.mention_html(),
                                exception=error.exception)
    return error.update.message.answer(text=i18n.errors.error(), reply_markup=inline.close())