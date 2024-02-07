from typing import Final
from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram_i18n import I18nContext

from ...database import database
from ...database.models import User
from ...keyboards import inline, data
from ...fsm import *

router: Final[Router] = Router(name=__name__)


@router.callback_query(F.data == data.AdminPanel.maintenance)
async def maintenance(call: types.CallbackQuery, user: User, state: FSMContext, i18n: I18nContext):
    await database.maintenance(True)
    await call.answer(i18n.messages.admin_success_maintenance())
    await call.message.edit_text(i18n.messages.admin_panel(),
                                 reply_markup=await inline.admin())
