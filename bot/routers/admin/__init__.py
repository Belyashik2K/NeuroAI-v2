from typing import Final

from aiogram import Router, F
from aiogram.enums import ChatType

from ...filters import IsAdmin
from . import admin_menu, find_user, neuro_statuses, maintenance

router: Final[Router] = Router(name=__name__)
router.include_routers(admin_menu.router, find_user.router,
                       neuro_statuses.router, maintenance.router)
router.message.filter(IsAdmin())
router.callback_query.filter(IsAdmin())
router.message.filter(F.chat.type == ChatType.PRIVATE)