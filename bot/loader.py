from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from .config import config
from .factories import Factory

def check_config() -> None:
    params = ["BOT_TOKEN", "FUTURE_FORGE_API_KEY",
              "technical_support", "ads", 
              "admin_chat", "admin_id", 
              "channel_link", "api_dev"]
    
    for param in params:
        if not getattr(config, param):
            raise ValueError(f"Parameter {param} is not set in config.py")
    if not config.ads.startswith("@") or not config.ads.startswith("@"):
        raise ValueError("Parameter ads must start with @. Edit config.py")
    if not config.channel_link.startswith("https://t.me/"):
        raise ValueError("Parameter channel_link must start with https://t.me/. Edit config.py")

check_config()

bot = Bot(token=config.BOT_TOKEN.get_secret_value(), parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())
factory = Factory(dp=dp)