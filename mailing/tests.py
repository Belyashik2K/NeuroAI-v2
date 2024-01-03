from .config import Config

from aiogram import __version__ as aiogram_version

class UnitTests:
    """Unit tests for mailing menu."""

    def __init__(self) -> None:
        """Initialize unit tests."""
        self._database = Config.UserDB.DB_INSTANCE
        self._bot = Config.Bot.BOT_INSTANCE
        self._version = aiogram_version
        self._attrs = ["get_admins", "get_users_count", "get_users_list"]

        self.__check_attrs()
        self.__check_bot()

    def __check_bot(self) -> None:
        """Check bot instance.
        
        If bot instance doesn't exist, raise AttributeError.
        If bot instance doesn't have aiogram attributes, raise AttributeError.
        If aiogram version is not 3.x.x, raise Exception.
        """
        if not self._bot:
            raise AttributeError("You didn't set your bot instance in config.py. Check the README.MD for more information.")
        if not hasattr(self._bot, "send_message"):
            raise AttributeError("Your bot instance doesn't have aiogram attributes. Check the README.MD for more information.")
        if not self._version.startswith("3."):
            raise Exception("Your aiogram version is not 3.x.x, but mailing menu works only with aiogram 3.x.x.")

    def __check_attrs(self) -> None:
        """Check database instance.
        
        If database instance doesn't exist, raise AttributeError.
        If database instance doesn't have necessary attributes, raise AttributeError.
        """
        if not self._database:
            raise AttributeError("You didn't set your database instance in config.py. Check the README.MD for more information.")
        for attr in self._attrs:
            if not hasattr(self._database, attr):
                raise AttributeError(f"Your database instance doesn't have '{attr}' attribute. Check the README.MD for more information.")