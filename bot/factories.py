from aiogram import Dispatcher
from aiogram_i18n import I18nMiddleware
from aiogram_i18n.cores import FluentRuntimeCore

from .middlewares import (UserMiddleware, 
                         ThrottlingMiddleware,
                         ChatMiddleware,
                         MaintenanceMiddleware,
                         UserManager,
                         BanMiddleware)

from .enums import Locale
from .utils import logging

class Factory:

    def __init__(self, 
                 dp: Dispatcher) -> None:
        self.__dp: Dispatcher = dp

    def middlewares(self) -> None:
        self.__dp.update.outer_middleware.register(ThrottlingMiddleware())
        self.__dp.update.outer_middleware.register(UserMiddleware())
        # TODO: Chat support
        # self.__dp.update.outer_middleware.register(ChatMiddleware())
        
        i18n_middleware = I18nMiddleware(
        core=FluentRuntimeCore(
            path="translations/{locale}",
            raise_key_error=False,
            locales_map={Locale.RU: Locale.EN, 
                         Locale.DE: Locale.EN,
                         Locale.UA: Locale.EN,
                         Locale.CN: Locale.EN,
                         Locale.HE: Locale.EN},
        ),
        manager=UserManager())
        i18n_middleware.setup(self.__dp)
        self.__dp.update.outer_middleware.register(BanMiddleware())
        self.__dp.update.outer_middleware.register(MaintenanceMiddleware())

    async def logging(self) -> None:
        await logging.setup()
