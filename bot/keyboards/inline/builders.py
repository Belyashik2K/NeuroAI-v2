from typing import Union

from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram_i18n import LazyProxy
from aiogram.types import Message, CallbackQuery
from aiogram_i18n.types import InlineKeyboardButton, InlineKeyboardMarkup

from ...enums import Locale, Mode, Category
from ...database.models import User
from ...config import config

from .callback import Callback, AllNeuros

class InlineKeyboards:

    def __init__(self) -> None:
        self.__first_page = "<<<"
        self.__previous_page = "<"
        self.__next_page = ">"
        self.__last_page = ">>>"

    def _pagination(self, 
                   buttons_data: str, 
                   pages_count: int, 
                   current_page: int) -> list[InlineKeyboardButton] | list:
        if pages_count > 1:   
            buttons = [
                InlineKeyboardButton(text=self.__previous_page, callback_data=buttons_data + str(current_page - 1) if current_page > 1 else Callback.Pagination.unavailable_page),
                InlineKeyboardButton(text=LazyProxy("buttons-pages_count", current=current_page, count=pages_count), callback_data=Callback.Pagination.show_page),
                InlineKeyboardButton(text=self.__next_page, callback_data=buttons_data + str(current_page + 1) if current_page < pages_count else Callback.Pagination.unavailable_page)
            ]

            if pages_count > 2:
                buttons.insert(0, InlineKeyboardButton(text=self.__first_page, callback_data=buttons_data + str(1) if current_page != 1 else Callback.Pagination.unavailable_page))
                buttons.append(InlineKeyboardButton(text=self.__last_page, callback_data=buttons_data + str(pages_count) if current_page != pages_count else Callback.Pagination.unavailable_page))

            return buttons
        return []

    def _locales(self, as_buttons: bool = False) -> InlineKeyboardMarkup | list[InlineKeyboardButton]:
        builder = InlineKeyboardBuilder()

        ru = InlineKeyboardButton(text=Locale.Buttons.RU, callback_data=Locale.RU)
        en = InlineKeyboardButton(text=Locale.Buttons.EN, callback_data=Locale.EN)
        de = InlineKeyboardButton(text=Locale.Buttons.DE, callback_data=Locale.DE)
        ua = InlineKeyboardButton(text=Locale.Buttons.UA, callback_data=Locale.UA)
        cn = InlineKeyboardButton(text=Locale.Buttons.CN, callback_data=Locale.CN)
        he = InlineKeyboardButton(text=Locale.Buttons.HE, callback_data=Locale.HE)
        
        if as_buttons:
            return [ru, en, de, ua, cn, he]
        builder.add(ru, en, de, ua, cn, he)
        builder.adjust(2, repeat=True)
        return builder.as_markup()
    
    def close(self, as_button: bool = False) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()
        close = InlineKeyboardButton(text=LazyProxy('buttons-close'), callback_data=Callback.close)
        if as_button:
            return close
        builder.add(close)
        return builder.as_markup()
    
    async def close_or_again(self,
                       neuro: str) -> InlineKeyboardMarkup:
        
        from ...database import database
        neuro_info = await database.get_neuro(neuro)

        builder = InlineKeyboardBuilder()
        again = InlineKeyboardButton(text=LazyProxy('buttons-again'),
                                     callback_data=Callback.Neuro(provider=neuro_info.provider,
                                                                  category=neuro_info.category,
                                                                  name=neuro_info.code_name).pack())
        close = self.close(as_button=True)

        builder.add(again, close)
        builder.adjust(1, 1)
        return builder.as_markup()
    
    def back(self, 
             callback_data: str,
             as_button: bool = False) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        back = InlineKeyboardButton(text=LazyProxy('buttons-back'), callback_data=callback_data)
        if as_button:
            return back
        builder.add(back)
        return builder.as_markup()
    
    def start(self) -> InlineKeyboardMarkup:
        return self._locales()
    
    def my_profile(self) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        change_language = InlineKeyboardButton(text=LazyProxy('buttons-set_language'), callback_data=Callback.Settings.set_language)
        
        builder.add(change_language, self.close(as_button=True))
        builder.adjust(1, repeat=True)

        return builder.as_markup()
    
    def settings(self) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        set_language = InlineKeyboardButton(text=LazyProxy('buttons-set_language'), callback_data=Callback.Settings.set_language)

        builder.add(set_language, self.close(as_button=True))
        builder.adjust(1, repeat=True)
        return builder.as_markup()

    def set_language(self) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        buttons = self._locales(True)

        builder.add(*buttons)
        builder.adjust(2, repeat=True)
        builder.row(self.back(Callback.Profile.back, as_button=True))
        return builder.as_markup()

    async def neuro_categories(self,
                               is_admin: bool = False) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        from ...database import database
        categories = await database.get_all_categories()

        for category in categories:
            text = LazyProxy(f'buttons-{category}')
            callback_data = Callback.Category(name=category).pack()
            builder.add(InlineKeyboardButton(text=text, callback_data=callback_data))

        builder.row(self.close(as_button=True) if not is_admin else self.back(Callback.AdminPanel.back, as_button=True))
        builder.adjust(2, 1, 1)

        return builder.as_markup()
    
    async def neuros(self,
                     category: str) -> InlineKeyboardMarkup:

        builder = InlineKeyboardBuilder()

        from ...database import database
        neuros = await database.get_neuros_by_category(category=category)

        for neuro in neuros:
            text = LazyProxy(f'buttons-{neuro.code_name}')
            callback_data = Callback.Neuro(provider=neuro.provider,
                                           category=neuro.category,
                                           name=neuro.code_name).pack()
            builder.add(InlineKeyboardButton(text=text, callback_data=callback_data))
        
        builder.adjust(2, repeat=True)
        builder.row(self.back(Callback.StartMenu.choose_neuro, as_button=True))

        return builder.as_markup()
    
    def mode(self) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        one_request = InlineKeyboardButton(text=LazyProxy('buttons-one_request'), callback_data=Callback.Mode(type_=Mode.ONE).pack())
        chat = InlineKeyboardButton(text=LazyProxy('buttons-chat'), callback_data=Callback.Mode(type_=Mode.CHAT).pack())

        builder.add(one_request, chat)
        builder.row(self.back(Callback.Category(name=Category.TEXT).pack(), as_button=True))
        builder.adjust(2, 1)
        return builder.as_markup()

    def about(self) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        channel = InlineKeyboardButton(text=LazyProxy('buttons-channel'), url=config.channel_link)
        future_forge = InlineKeyboardButton(text=LazyProxy('buttons-future_forge'), url="https://api.futureforge.dev/docs")
        vision_craft = InlineKeyboardButton(text=LazyProxy('buttons-vision_craft'), url="https://visioncraft-rs24.koyeb.app/docs")
        source = InlineKeyboardButton(text=LazyProxy('buttons-source'), url="https://github.com/Belyashik2K/NeuroAI-v2")

        builder.add(channel, future_forge, vision_craft, source)
        builder.row(self.close(as_button=True))
        builder.adjust(1, 2, 1)
        return builder.as_markup()
    
    async def admin(self) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        statuses = [
            LazyProxy('buttons-maintenance-enable'),
            LazyProxy('buttons-maintenance-disable')
        ]

        from ...database import database
        maintenance_status = await database.maintenance()

        find_user = InlineKeyboardButton(text=LazyProxy('buttons-find_user'), callback_data=Callback.AdminPanel.find_user)
        mailing = InlineKeyboardButton(text=LazyProxy('buttons-mailing'), callback_data=Callback.AdminPanel.mailing)
        change_neuro = InlineKeyboardButton(text=LazyProxy('buttons-change_neuro'), callback_data=Callback.AdminPanel.change_neuro)
        maintenance = InlineKeyboardButton(text=statuses[maintenance_status], callback_data=Callback.AdminPanel.maintenance)

        builder.add(find_user, mailing, change_neuro, maintenance)
        builder.adjust(2, 1, 1)
        builder.row(self.close(as_button=True))
        return builder.as_markup()
        
    def all_neuros(self,
                   category: str) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        for neuro, data in AllNeuros.data[category].items():
            callback_data = Callback.Neuros.switch + data.replace(Callback.Neuros.start, '')
            builder.button(text=neuro, callback_data=callback_data)
        
        builder.adjust(2, repeat=True)
        builder.row(self.back(Callback.AdminPanel.change_neuro, as_button=True))

        return builder.as_markup()
    
    async def user_actions(self, 
                     user: User,
                     instance: Union[Message, CallbackQuery]) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        bans = [
            LazyProxy('buttons-bans-ban'),
            LazyProxy('buttons-bans-unban'),
        ]

        admins = [
            LazyProxy('buttons-admins-add'),
            LazyProxy('buttons-admins-remove'),
        ]

        ban = InlineKeyboardButton(text=bans[user.is_banned], callback_data=Callback.AdminPanel.ban + str(user.user_id))
        admin = InlineKeyboardButton(text=admins[user.is_admin], callback_data=Callback.AdminPanel.admin + str(user.user_id))
        builder.add(ban, admin)

        info = await instance.bot.get_chat(user.user_id)
        if not (info.has_private_forwards and not info.username):
            mention = InlineKeyboardButton(text=LazyProxy('buttons-mention'), url=user.url)
            builder.add(mention)
            
        builder.row(self.back(Callback.AdminPanel.back, as_button=True))
        builder.adjust(1, repeat=True)

        return builder.as_markup()
    
    def start(self) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        choose_neuro = InlineKeyboardButton(text=LazyProxy('buttons-neuro_choose'), callback_data=Callback.StartMenu.choose_neuro)
        my_account = InlineKeyboardButton(text=LazyProxy('buttons-my_account'), callback_data=Callback.StartMenu.my_account)
        stats = InlineKeyboardButton(text=LazyProxy('buttons-stats'), callback_data=Callback.StartMenu.stats)
        about = InlineKeyboardButton(text=LazyProxy('buttons-about'), callback_data=Callback.StartMenu.about)

        builder.add(choose_neuro, my_account, stats, about)
        builder.row(self.close(as_button=True))
        builder.adjust(1, 2, 1, 1)

        return builder.as_markup() 
    
    def autotranscription(self, 
                          status: bool) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        autotrans = [
            LazyProxy('buttons-autotrans-disable'),
            LazyProxy('buttons-autotrans-enable')
        ]

        builder.button(text=autotrans[status], callback_data=Callback.Chat.autotrans)

        return builder.as_markup()
