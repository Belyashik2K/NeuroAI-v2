from typing import Final

from aiogram import Router, F
from aiogram.enums import ChatType

from . import (start, 
               settings, 
               about_service, 
               stats,
               profile,
               neuros)

router: Final[Router] = Router(name=__name__)
router.include_routers(start.router, settings.router, 
                       about_service.router, stats.router,
                       profile.router, neuros.router)
router.message.filter(F.chat.type == ChatType.PRIVATE)

