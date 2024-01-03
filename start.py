import asyncio
import logging
import os

from aiogram.types.error_event import ErrorEvent
from aiogram.fsm.context import FSMContext

from texts import ET
from initialization import bot, dp
from database import database
from middlewares import register_middlewares
from keyboards import reply
from notify import AdminNotify
from mailing import *

async def main():

    if not os.path.isdir("logging"):
        os.mkdir("logging")

    logging.basicConfig(filename='logging/bot.log',
                        encoding='utf-8',
                        level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s', 
                        datefmt='%d.%m.%Y %H:%M:%S')
    
    notify = AdminNotify()

    from routers import all_routers
    all_routers.insert(0, mailing_router)
    dp.include_routers(*all_routers)

    register_middlewares(dp=dp)

    @dp.errors()
    async def errors_handler(error: ErrorEvent, state: FSMContext):
        if "message is not modified" in str(error.exception).lower():
            return True
        user = await database.get_user(user_id=error.update.message.from_user.id)
        await error.update.bot.send_message(chat_id=error.update.message.chat.id, 
                                            text=ET.error, 
                                            reply_markup=await reply.get_start_keyboard(user=user))
        await state.clear()
        await notify.error_notify(user_id=user.user_id,
                                  mention=error.update.message.from_user.mention_html(),
                                  exception=error.exception)
        return True
    
    await database.create_tables()
    await bot.delete_webhook(drop_pending_updates=True)
    me = await bot.me()
    print(f"Bot @{me.username} started.")
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info('Bot stopped.')
    except Exception as e:
        logging.exception(e)