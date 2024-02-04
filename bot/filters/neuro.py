from aiogram.types import CallbackQuery
from aiogram.filters import BaseFilter

from aiogram_i18n import LazyProxy

from ..database import database
from ..keyboards import data

class isNeuroActive(BaseFilter):
    async def __call__(self, call: CallbackQuery, callback_data: data.Neuro) -> bool:
        neuro = await database.get_neuro(callback_data.name)
        if not neuro.is_active:
            await call.answer(LazyProxy('errors-neuro_on_maintenance').data, show_alert=True)
            return False
        return True