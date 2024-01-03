from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from config import Config

def check_config() -> None:
    params = ["BOT_TOKEN", "DB_PATH", "SECRET_KEY", 
              "technical_support", "ads", "admin_chat", 
              "channel_link", "admin_id"]
    
    for param in params:
        if not getattr(Config, param):
            raise ValueError(f"Parameter {param} is not set in config.py")
    if not Config.ads.startswith("@") or not Config.ads.startswith("@"):
        raise ValueError("Parameter ads must start with @. Edit config.py")
    if not Config.channel_link.startswith("https://t.me/"):
        raise ValueError("Parameter channel_link must start with https://t.me/. Edit config.py")

check_config()

bot = Bot(token=Config.BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())