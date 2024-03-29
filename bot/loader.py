from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from .config import config
from .factories import Factory
from .middlewares import RetryRequestMiddleware
from .utils import msgspec_json


def check_config() -> None:
    params = ["BOT_TOKEN", "FUTURE_FORGE_API_KEY",
              "VISION_CRAFT_API_KEY",
              "technical_support", "ads",
              "admin_chat", "admin_id",
              "channel_link"]

    for param in params:
        if not getattr(config, param):
            raise ValueError(f"Parameter {param} is not set in config.py")
    if not config.ads.startswith("@") or not config.ads.startswith("@"):
        raise ValueError("Parameter ads must start with @. Edit config.py")
    if not config.channel_link.startswith("https://t.me/"):
        raise ValueError("Parameter channel_link must start with https://t.me/. Edit config.py")


check_config()

session: AiohttpSession = AiohttpSession(json_loads=msgspec_json.decode,
                                         json_dumps=msgspec_json.encode)
session.middleware(RetryRequestMiddleware())

bot = Bot(token=config.BOT_TOKEN.get_secret_value(),
          session=session,
          parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())
factory = Factory(dp=dp)
