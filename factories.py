from aiogram import Dispatcher

from routers import (chat_router)
from middlewares import (UserMiddleware,
                         ThrottlingMiddleware,
                         MaintenanceMiddleware,
                         ChatMiddleware)

class Factories:

    def middlewares(self, dp: Dispatcher):
        """Register all middlewares."""
        dp.message.middleware(UserMiddleware())
        dp.callback_query.middleware(UserMiddleware())
        dp.message.middleware(ThrottlingMiddleware())
        dp.message.middleware(MaintenanceMiddleware())
        dp.callback_query.middleware(MaintenanceMiddleware())
        chat_router.message.middleware(ChatMiddleware())
        chat_router.callback_query.middleware(ChatMiddleware())
