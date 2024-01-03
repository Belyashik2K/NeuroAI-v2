from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from texts import IB, RB, AN
from database import database as db
from config import Config
from database.models import User

class InlineKeyboards: 
    
    def __init__(self) -> None:
        self._close = InlineKeyboardButton(text=IB.close, callback_data=IB.Callback.close)

    async def get_close_keyboard(self) -> InlineKeyboardMarkup:
        """Generate close keyboard
        
        Returns:
            InlineKeyboardMarkup: Close keyboard."""
        k = InlineKeyboardBuilder()
        k.add(self._close)
        return k.as_markup()
    
    async def get_back_button(self, callback_data: str) -> InlineKeyboardButton:
        """Generate back button.
        
        Args:
            callback_data (str): Callback data.
            
        Returns:
            InlineKeyboardButton: Back button."""
        back = InlineKeyboardButton(text=IB.back, callback_data=callback_data)
        return back
    
    async def get_back_keyboard(self, callback_data: str) -> InlineKeyboardMarkup:
        """Generate back keyboard.
        
        Args:
            callback_data (str): Callback data.
            
        Returns:
            InlineKeyboardMarkup: Back keyboard."""
        k = InlineKeyboardBuilder()
        k.add(await self.get_back_button(callback_data=callback_data))
        return k.as_markup()
    
    async def choose_category_keyboard(self) -> InlineKeyboardMarkup:
        """Generate keyboard with neuro categories.
        
        Returns:
            InlineKeyboardMarkup: Keyboard with neuro categories."""
        
        k = InlineKeyboardBuilder()
        k.button(text=IB.NeuroCategories.text, callback_data=IB.Callback.NeuroCategories.text)
        k.button(text=IB.NeuroCategories.image, callback_data=IB.Callback.NeuroCategories.image)
        k.button(text=IB.NeuroCategories.audio, callback_data=IB.Callback.NeuroCategories.audio)
        k.add(self._close)

        k.adjust(2, 1, 1)

        return k.as_markup()
    
    async def choose_neuro_keyboard(self, 
                                    category: str
                                    ) -> InlineKeyboardMarkup:
        """Generate keyboard with neuros by given category.
        
        Args:
            category (str): Category of neuros.
            
        Returns:
            InlineKeyboardMarkup: Keyboard with neuros."""
        
        k = InlineKeyboardBuilder()

        categories = {
            IB.Callback.NeuroCategories.text: [InlineKeyboardButton(text=IB.Neuros.gpt, callback_data=IB.Callback.Neuros.gpt),
                                      InlineKeyboardButton(text=IB.Neuros.claude, callback_data=IB.Callback.Neuros.claude),
                                      InlineKeyboardButton(text=IB.Neuros.google, callback_data=IB.Callback.Neuros.google),
                                      InlineKeyboardButton(text=IB.Neuros.llama, callback_data=IB.Callback.Neuros.llama),
                                      InlineKeyboardButton(text=IB.Neuros.mistral, callback_data=IB.Callback.Neuros.mistral),
                                      InlineKeyboardButton(text=IB.Neuros.gemini, callback_data=IB.Callback.Neuros.gemini)],
            IB.Callback.NeuroCategories.image: [InlineKeyboardButton(text=IB.Neuros.stable, callback_data=IB.Callback.Neuros.stable),
                                       InlineKeyboardButton(text=IB.Neuros.playground, callback_data=IB.Callback.Neuros.playground),
                                       InlineKeyboardButton(text=IB.Neuros.enhance, callback_data=IB.Callback.Neuros.enhance),
                                       InlineKeyboardButton(text=IB.Neuros.midjourney, callback_data=IB.Callback.Neuros.midjourney),
                                       InlineKeyboardButton(text=IB.Neuros.sdv, callback_data=IB.Callback.Neuros.sdv),
                                       InlineKeyboardButton(text=IB.Neuros.dalle3, callback_data=IB.Callback.Neuros.dalle3)],
            IB.Callback.NeuroCategories.audio: [InlineKeyboardButton(text=IB.Neuros.whisper, callback_data=IB.Callback.Neuros.whisper),
                                        InlineKeyboardButton(text=IB.Neuros.bender, callback_data=IB.Callback.Neuros.bender)]
                }
        for button in categories[category]:
            k.add(button)

        k.adjust(2, repeat=True)

        k.row(await self.get_back_button(callback_data=IB.Callback.NeuroCategories.back))

        return k.as_markup()
    
    async def choose_mode_keyboard(self, ) -> InlineKeyboardMarkup:
        """Generate keyboard with modes for text neuros."""
    
        k = InlineKeyboardBuilder()
        k.button(text=IB.Mode.one_request, callback_data=IB.Callback.Mode.one_request)
        k.button(text=IB.Mode.chat, callback_data=IB.Callback.Mode.chat)
        k.row(await self.get_back_button(callback_data=IB.Callback.NeuroCategories.text))
        k.adjust(2, 1)
        return k.as_markup()
    
    async def get_about_keyboard(self) -> InlineKeyboardMarkup:
        """Generate keyboard with links.
        
        Returns:
            InlineKeyboardMarkup: Keyboard with links."""
        
        k = InlineKeyboardBuilder()
        k.button(text=IB.Links.channel, url=Config.channel_link)
        k.button(text=IB.Links.api_dev, url=Config.api_dev)
        k.row(self._close)
        k.adjust(2, 1)
        return k.as_markup()
    
    async def get_admin_keyboard(self) -> InlineKeyboardMarkup:
        """Generate keyboard for admin.
        
        Returns:
            InlineKeyboardMarkup: Keyboard for admin."""
        k = InlineKeyboardBuilder()
        k.button(text=IB.AdminPanel.change_neuro, callback_data=IB.Callback.AdminPanel.change_neuro)
        k.button(text=IB.AdminPanel.find_user, callback_data=IB.Callback.AdminPanel.find_user)
        k.button(text=IB.AdminPanel.mailing, callback_data=IB.Callback.AdminPanel.mailing)
        k.button(text=IB.AdminPanel.maintenance[await db.maintenance()], callback_data=IB.Callback.AdminPanel.maintenance)
        k.row(self._close)
        k.adjust(2, 1, 1)
        return k.as_markup()
    
    async def get_all_neuros_keyboard(self) -> InlineKeyboardMarkup:
        """Generate keyboard with all neuros.
        
        Returns:
            InlineKeyboardMarkup: Keyboard with all neuros."""
        k = InlineKeyboardBuilder()

        for neuro, data in AN.data.items():
            callback_data = IB.Callback.Neuros.switch + data.replace(IB.Callback.Neuros.start, '')
            k.button(text=neuro, callback_data=callback_data)
        
        k.row(await self.get_back_button(callback_data=IB.Callback.AdminPanel.back))
        k.adjust(2, repeat=True)

        return k.as_markup()
    
    async def get_user_keyboard(self, user: User) -> InlineKeyboardMarkup:
        """Generate keyboard for user info.
        
        Args:
            user (User): User object.
            
        Returns:
            InlineKeyboardMarkup: Keyboard for user info."""
        
        ban_button = InlineKeyboardButton(text=IB.AdminPanel.bans[user.is_banned], callback_data=IB.Callback.AdminPanel.ban + str(user.user_id))
        admin_button = InlineKeyboardButton(text=IB.AdminPanel.admins[user.is_admin], callback_data=IB.Callback.AdminPanel.admin + str(user.user_id))
        k = InlineKeyboardBuilder()
        k.add(ban_button, admin_button)
        k.adjust(1, repeat=True)
        k.row(await self.get_back_button(callback_data=IB.Callback.AdminPanel.back))

        return k.as_markup()
    
    async def get_start_keyboard(self) -> InlineKeyboardMarkup:
        """Generate start keyboard.
        
        Returns:
            InlineKeyboardMarkup: Start keyboard."""
        k = InlineKeyboardBuilder()

        k.button(text=RB.neuro_choose, callback_data=IB.Callback.StartMenu.choose_neuro)
        k.button(text=RB.my_account, callback_data=IB.Callback.StartMenu.my_account)
        k.button(text=RB.stats, callback_data=IB.Callback.StartMenu.stats)
        k.button(text=RB.about, callback_data=IB.Callback.StartMenu.about)
        k.row(self._close)

        k.adjust(1, 2, 1, 1)

        return k.as_markup()
        