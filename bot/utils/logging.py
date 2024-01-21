import logging
import os

from ..config import config

async def setup():
    from ..loader import bot
    bot_info = await bot.get_me()
    
    if not os.path.exists('./logging'):
        os.mkdir('./logging')

    logging.basicConfig(
        filename=f'./logging/@{bot_info.username}.log',
        encoding='utf-8',
        level=logging.DEBUG if config.is_debug else logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%d-%b-%y %H:%M:%S'
    )

    print("Bot {} started at @{}".format(bot_info.full_name, bot_info.username))
    print("Link >>> https://t.me/", bot_info.username, sep="")