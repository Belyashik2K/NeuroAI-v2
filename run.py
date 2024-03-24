import asyncio

from bot import mailing
from bot.loader import bot, dp, factory
from bot.database import database
from bot.routers import admin, extra, main


async def startup() -> None:
    dp.include_routers(main.router,
                       mailing.router,
                       admin.router,
                       extra.router)

    factory.middlewares()
    await factory.logging()
    await database.prepare()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(startup())
