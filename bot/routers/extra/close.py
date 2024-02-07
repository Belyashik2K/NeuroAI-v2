from typing import Final

from aiogram import Router, F, types

from ...keyboards import data

router: Final[Router] = Router(name=__name__)


@router.callback_query(F.data == data.close)
async def close(call: types.CallbackQuery):
    await call.message.delete()
