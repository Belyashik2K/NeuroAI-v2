from typing import Final

from aiogram import Router, F, types

from ...keyboards import data

router: Final[Router] = Router(name=__name__)


@router.callback_query(F.data == data.close)
async def close(call: types.CallbackQuery):
    if call.message.reply_to_message:
        await call.message.bot.delete_message(chat_id=call.message.chat.id, 
                                              message_id=call.message.reply_to_message.message_id)
    await call.message.delete()
