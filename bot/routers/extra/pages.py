from typing import Final

from aiogram import F, Router
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from ...keyboards import data

router: Final[Router] = Router(name=__name__)


@router.callback_query(F.data == data.Pagination.unavailable_page)
async def unavailable_page(call: CallbackQuery, i18n: I18nContext):
    await call.answer(i18n.errors.unavailable_page())


@router.callback_query(F.data == data.Pagination.show_page)
async def show_page(call: CallbackQuery, i18n: I18nContext):
    for row in call.message.reply_markup.inline_keyboard[::-1]:
        for button in row:
            if button.callback_data == call.data:
                text = button.text
                break
    await call.answer(text, True)
