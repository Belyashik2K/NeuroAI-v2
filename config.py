import os

from dotenv import load_dotenv

load_dotenv()

class Config(object):
    """Config class for bot."""
    # CHECK README.md FOR MORE INFORMATION
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") # Bot token from @BotFather
    DB_PATH = os.environ.get("DB_PATH", "") # Path to database
    SECRET_KEY = os.environ.get("SECRET_KEY", "") # Secret key from ImageBan API

    technical_support = "@Belyashik2K" # Technical support username with @
    ads = "@Belyashik2K" # Ads-manager/creator username with @

    admin_chat = -1001111111 # Admin user/chat id for notifications
    admin_id = 111111111 # ID for first admin (for "👨‍💻 Админ-панель" button")

    channel_link = "https://t.me/NeuroAIchannel" # Channel link for "📢 Наш канал" button
    api_dev = "https://api.futureforge.dev/docs" # Please, don't change this link. Support the work of the author of the API. Thank you!