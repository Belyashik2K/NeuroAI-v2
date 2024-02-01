from typing import Union

from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram_i18n import LazyProxy
from aiogram.types import Message, CallbackQuery
from aiogram_i18n.types import InlineKeyboardButton, InlineKeyboardMarkup

from ...enums import Locale
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
    
    def close_or_again(self,
                       neuro: str) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()
        again = InlineKeyboardButton(text=LazyProxy('buttons-again'),
                                     callback_data=neuro)
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

    def neuro_categories(self,
                         is_admin: bool = False) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        text = InlineKeyboardButton(text=LazyProxy('buttons-text'), callback_data=Callback.NeuroCategories.text if not is_admin else Callback.NeuroCategories.admin + Callback.NeuroCategories.text)
        image = InlineKeyboardButton(text=LazyProxy('buttons-image'), callback_data=Callback.NeuroCategories.image if not is_admin else Callback.NeuroCategories.admin + Callback.NeuroCategories.image)
        audio = InlineKeyboardButton(text=LazyProxy('buttons-audio'), callback_data=Callback.NeuroCategories.audio if not is_admin else Callback.NeuroCategories.admin + Callback.NeuroCategories.audio)

        builder.add(text, image, audio)
        builder.row(self.close(as_button=True) if not is_admin else self.back(Callback.AdminPanel.back, as_button=True))
        builder.adjust(2, 1, 1)
        return builder.as_markup()
    
    def neuros(self,
               category: str) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        categories = {
            Callback.NeuroCategories.text: [InlineKeyboardButton(text=LazyProxy('buttons-gpt'), callback_data=Callback.Neuros.gpt),
                                    InlineKeyboardButton(text=LazyProxy('buttons-claude'), callback_data=Callback.Neuros.claude),
                                    InlineKeyboardButton(text=LazyProxy('buttons-google'), callback_data=Callback.Neuros.google),
                                    InlineKeyboardButton(text=LazyProxy('buttons-llama'), callback_data=Callback.Neuros.llama),
                                    InlineKeyboardButton(text=LazyProxy('buttons-mistral'), callback_data=Callback.Neuros.mistral),
                                    InlineKeyboardButton(text=LazyProxy('buttons-solar'), callback_data=Callback.Neuros.solar),     InlineKeyboardButton(text=LazyProxy('buttons-gemini'), callback_data=Callback.Neuros.gemini)],
            Callback.NeuroCategories.image: [InlineKeyboardButton(text=LazyProxy('buttons-stable'), callback_data=Callback.Neuros.stable),
                                    InlineKeyboardButton(text=LazyProxy('buttons-playground'), callback_data=Callback.Neuros.playground),
                                    InlineKeyboardButton(text=LazyProxy('buttons-midjourney'), callback_data=Callback.Neuros.midjourney),
                                    InlineKeyboardButton(text=LazyProxy('buttons-midjourneyv6'), callback_data=Callback.Neuros.midjourneyv6),
                                    InlineKeyboardButton(text=LazyProxy('buttons-enhance'), callback_data=Callback.Neuros.enhance),
                                    InlineKeyboardButton(text=LazyProxy('buttons-sdv'), callback_data=Callback.Neuros.sdv),
                                    InlineKeyboardButton(text=LazyProxy('buttons-dalle3'), callback_data=Callback.Neuros.dalle3),
                                    InlineKeyboardButton(text=LazyProxy('buttons-tencentmaker'), callback_data=Callback.Neuros.tencentmaker),
                                    InlineKeyboardButton(text=LazyProxy('buttons-juggernaut'), callback_data=Callback.Neuros.juggernaut),
                                    InlineKeyboardButton(text=LazyProxy('buttons-dynavision'), callback_data=Callback.Neuros.dynavision),
                                    InlineKeyboardButton(text=LazyProxy('buttons-animeart'), callback_data=Callback.Neuros.animeart)],
            Callback.NeuroCategories.audio: [InlineKeyboardButton(text=LazyProxy('buttons-whisper'), callback_data=Callback.Neuros.whisper),
                                    InlineKeyboardButton(text=LazyProxy('buttons-bender'), callback_data=Callback.Neuros.bender)]
                }
        for button in categories[category]:
            builder.add(button)

        builder.adjust(2, repeat=True)

        builder.row(self.back(Callback.NeuroCategories.back, as_button=True))

        return builder.as_markup()
    
    def mode(self) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        one_request = InlineKeyboardButton(text=LazyProxy('buttons-one_request'), callback_data=Callback.Mode.one_request)
        chat = InlineKeyboardButton(text=LazyProxy('buttons-chat'), callback_data=Callback.Mode.chat)

        builder.add(one_request, chat)
        builder.row(self.back(Callback.NeuroCategories.text, as_button=True))
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
