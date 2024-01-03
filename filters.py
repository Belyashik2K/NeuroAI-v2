from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery, Update

from database import database as db
from texts import ET

class IsAdmin(BaseFilter):
    async def __call__(self, update: Update) -> bool:
        user = await db.get_user(user_id=update.from_user.id)
        return user.is_admin
    
class isNeuroActive(BaseFilter):
    async def __call__(self, call: CallbackQuery) -> bool:
        neuro = await db.get_neuro(call.data.split('_')[1])
        if not neuro.is_active:
            await call.answer(ET.neuro_on_maintenance, show_alert=True)
            return False
        return True