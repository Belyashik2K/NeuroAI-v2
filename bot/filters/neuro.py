from aiogram.types import CallbackQuery
from aiogram.filters import BaseFilter

from aiogram_i18n import LazyProxy

from ..database import database

class isNeuroActive(BaseFilter):
    async def __call__(self, call: CallbackQuery) -> bool:
        neuro = await database.get_neuro(call.data.split('_')[1])
        if not neuro.is_active:
            await call.answer(LazyProxy('errors-neuro_on_maintenance').data, show_alert=True)
            return False
        return True