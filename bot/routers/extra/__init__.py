from typing import Final

from aiogram import Router, F
from aiogram.enums import ChatType

from . import errors, close, pages, unknown

router: Final[Router] = Router(name=__name__)
router.include_routers(close.router, pages.router, errors.router, unknown.router)
router.message.filter(F.chat.type == ChatType.PRIVATE)
