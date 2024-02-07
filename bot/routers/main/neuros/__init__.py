from typing import Final

from aiogram import Router

from . import select, request

router: Final[Router] = Router(name=__name__)
router.include_routers(select.router, request.router)
