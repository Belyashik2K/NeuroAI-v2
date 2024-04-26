from typing import Union, Callable, Type, Awaitable

from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram_i18n import LazyProxy
from aiogram.types import Message, CallbackQuery
from aiogram_i18n.types import InlineKeyboardButton, InlineKeyboardMarkup

from ...enums import Locale, Mode, Category, Actions, Task
from ...database.models import User
from ...config import config

from .callback import Callback


class InlineKeyboards:

    def __init__(self) -> None:
        self.__first_page = "<<<"
        self.__previous_page = "<"
        self.__next_page = ">"
        self.__last_page = ">>>"

    def _pagination(self,
                    data_object: Callable[[Type[CallbackData]], Awaitable[CallbackData]],
                    pages_count: int,
                    current_page: int,
                    **kwargs: object) -> list[InlineKeyboardButton] | list:
        if pages_count > 1:
            buttons = [
                InlineKeyboardButton(text=self.__previous_page, callback_data=data_object(**kwargs,
                                                                                          page=current_page - 1).pack() if current_page > 1 else Callback.Pagination.unavailable_page),
                InlineKeyboardButton(text=LazyProxy("buttons-pages_count", current=current_page, count=pages_count),
                                     callback_data=Callback.Pagination.show_page),
                InlineKeyboardButton(text=self.__next_page, callback_data=data_object(**kwargs,
                                                                                      page=current_page + 1).pack() if current_page < pages_count else Callback.Pagination.unavailable_page)
            ]

            if pages_count > 2:
                buttons.insert(0, InlineKeyboardButton(text=self.__first_page, callback_data=data_object(**kwargs,
                                                                                                         page=1).pack() if current_page != 1 else Callback.Pagination.unavailable_page))
                buttons.append(InlineKeyboardButton(text=self.__last_page, callback_data=data_object(**kwargs,
                                                                                                     page=pages_count).pack() if current_page != pages_count else Callback.Pagination.unavailable_page))

            return buttons
        return []

    @staticmethod
    def _locales(as_buttons: bool = False) -> InlineKeyboardMarkup | list[InlineKeyboardButton]:
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

    @staticmethod
    def close(as_button: bool = False) -> InlineKeyboardMarkup | InlineKeyboardButton:
        builder = InlineKeyboardBuilder()
        close = InlineKeyboardButton(text=LazyProxy('buttons-close'), callback_data=Callback.close)
        if as_button:
            return close
        builder.add(close)
        return builder.as_markup()

    @staticmethod
    def back(callback_data: str,
             as_button: bool = False) -> InlineKeyboardMarkup | InlineKeyboardButton:
        builder = InlineKeyboardBuilder()

        back = InlineKeyboardButton(text=LazyProxy('buttons-back'),
                                    callback_data=callback_data)
        if as_button:
            return back
        builder.add(back)
        return builder.as_markup()
    
    def tech_supp(self) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()
        
        url = "https://t.me/{}".format(config.technical_support[1:])

        tech_supp = InlineKeyboardButton(text=LazyProxy('buttons-technical_support'),
                                        url=url)
        builder.add(tech_supp)
        builder.row(self.close(True))
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

    def my_profile(self) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        change_language = InlineKeyboardButton(text=LazyProxy('buttons-set_language'),
                                               callback_data=Callback.Settings.set_language)

        builder.add(change_language, self.close(as_button=True))
        builder.adjust(1, repeat=True)

        return builder.as_markup()

    def settings(self) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        set_language = InlineKeyboardButton(text=LazyProxy('buttons-set_language'),
                                            callback_data=Callback.Settings.set_language)

        builder.add(set_language, self.close(as_button=True))
        builder.adjust(1, repeat=True)
        return builder.as_markup()

    def set_language(self) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        buttons = self._locales(True)

        builder.add(*buttons)
        builder.adjust(2, repeat=True)
        builder.row(self.back(Callback.StartMenu.my_account, as_button=True))
        return builder.as_markup()

    async def neuro_categories(self,
                               is_admin: bool = False) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        from ...database import database
        categories = await database.get_all_categories()

        for category in categories:
            text = LazyProxy(f'buttons-{category}')
            callback_data = Callback.Category(name=category, page=1).pack() if not is_admin else Callback.AdminCategory(
                name=category, page=1).pack()
            builder.add(InlineKeyboardButton(text=text, callback_data=callback_data))

        favourite = InlineKeyboardButton(text=LazyProxy('buttons-favourite'), callback_data=Callback.StartMenu.favourite)

        if not is_admin:
            builder.add(favourite)
        builder.row(self.close(as_button=True) if not is_admin else self.back(Callback.StartMenu.admin, as_button=True))
        builder.adjust(2, 1, 1)

        return builder.as_markup()

    async def neuros(self,
                     category: str,
                     page: int,
                     is_admin: bool = False) -> InlineKeyboardMarkup:

        builder = InlineKeyboardBuilder()

        from ...database import database
        neuros, pages_count = await database.get_neuros_by_category(category=category,
                                                                    page=page,
                                                                    per_page=6)
        status = {
            True: LazyProxy('messages-working').data,
            False: LazyProxy('messages-not_working').data
        }
        for neuro in neuros:
            text = LazyProxy(f'buttons-{neuro.code_name}').data + f" ({status[neuro.is_active]})"
            if not is_admin:
                callback_data = Callback.Neuro(provider=neuro.provider,
                                               category=neuro.category,
                                               name=neuro.code_name).pack()
            else:
                callback_data = Callback.Switch(neuro_name=neuro.code_name).pack()
            builder.add(InlineKeyboardButton(text=text, callback_data=callback_data))
        builder.adjust(2, repeat=True)

        pagination = self._pagination(data_object=Callback.Category if not is_admin else Callback.AdminCategory,
                                      pages_count=pages_count,
                                      current_page=page,
                                      name=category)

        builder.row(*pagination)
        builder.row(self.back(Callback.StartMenu.choose_neuro, as_button=True) if not is_admin else self.back(
            Callback.AdminPanel.change_neuro, as_button=True))

        return builder.as_markup()

    def mode(self,
             neuro_name: str,
             page: int,
             in_favourite: bool,
             from_fav: bool) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()
        
        fav = {
            True: (LazyProxy('buttons-remove_fav'), Actions.REMOVE),
            False: (LazyProxy('buttons-add_fav'), Actions.ADD)
        }

        one_request = InlineKeyboardButton(text=LazyProxy('buttons-one_request'),
                                           callback_data=Callback.Mode(type_=Mode.ONE).pack())
        chat = InlineKeyboardButton(text=LazyProxy('buttons-chat'), callback_data=Callback.Mode(type_=Mode.CHAT).pack())

        builder.add(one_request, chat)
        builder.add(InlineKeyboardButton(text=fav[in_favourite][0], 
                                         callback_data=Callback.Favourite(neuro_name=neuro_name,
                                                                          category=Category.TEXT,
                                                                          action=fav[in_favourite][1]
                                                                          ).pack())) 
        if from_fav:
            builder.row(self.back(Callback.FavouritePagination(page=page).pack(), as_button=True))
        else:
            builder.row(self.back(Callback.Category(name=Category.TEXT, page=page).pack(), as_button=True))
        builder.adjust(2, 1)
        return builder.as_markup()
    
    def image_or_voice(self, 
                       category: str,
                       neuro_name: str,
                       in_favourite: bool,
                       from_fav: bool,
                       page: int) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()
        
        fav = {
            True: (LazyProxy('buttons-remove_fav'), Actions.REMOVE),
            False: (LazyProxy('buttons-add_fav'), Actions.ADD)
        }
        
        builder.add(InlineKeyboardButton(text=fav[in_favourite][0],
                                         callback_data=Callback.Favourite(neuro_name=neuro_name,
                                                                          category=category,
                                                                          action=fav[in_favourite][1]
                                                                          ).pack()))
        if from_fav:
            builder.row(self.back(Callback.FavouritePagination(page=page).pack(), as_button=True))
        else:
            builder.row(self.back(Callback.Category(name=category, 
                                                    page=page
                                                    ).pack(), as_button=True))
        return builder.as_markup()

    def about(self) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        channel = InlineKeyboardButton(text=LazyProxy('buttons-channel'), url=config.channel_link)
        future_forge = InlineKeyboardButton(text=LazyProxy('buttons-future_forge'),
                                            url="https://api.futureforge.dev/docs")
        vision_craft = InlineKeyboardButton(text=LazyProxy('buttons-vision_craft'),
                                            url="https://api.visioncraft.top/docs")
        source = InlineKeyboardButton(text=LazyProxy('buttons-source'),
                                      url="https://github.com/Belyashik2K/NeuroAI-v2")

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

        find_user = InlineKeyboardButton(text=LazyProxy('buttons-find_user'),
                                         callback_data=Callback.AdminPanel.find_user)
        mailing = InlineKeyboardButton(text=LazyProxy('buttons-mailing'), callback_data=Callback.AdminPanel.mailing)
        change_neuro = InlineKeyboardButton(text=LazyProxy('buttons-change_neuro'),
                                            callback_data=Callback.AdminPanel.change_neuro)
        maintenance = InlineKeyboardButton(text=statuses[maintenance_status],
                                           callback_data=Callback.AdminPanel.maintenance)

        builder.add(find_user, mailing, change_neuro, maintenance)
        builder.adjust(2, 1, 1)
        builder.row(self.close(as_button=True))
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

        ban = InlineKeyboardButton(text=bans[user.is_banned],
                                   callback_data=Callback.BanUser(user_id=user.user_id).pack())
        admin = InlineKeyboardButton(text=admins[user.is_admin],
                                     callback_data=Callback.AdminUser(user_id=user.user_id).pack())
        builder.add(ban, admin)

        info = await instance.bot.get_chat(user.user_id)
        if not (info.has_private_forwards and not info.username):
            mention = InlineKeyboardButton(text=LazyProxy('buttons-mention'), url=user.url)
            builder.add(mention)

        builder.row(self.back(Callback.StartMenu.admin, as_button=True))
        builder.adjust(1, repeat=True)

        return builder.as_markup()

    def start(self) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        choose_neuro = InlineKeyboardButton(text=LazyProxy('buttons-neuro_choose'),
                                            callback_data=Callback.StartMenu.choose_neuro)
        my_account = InlineKeyboardButton(text=LazyProxy('buttons-my_account'),
                                          callback_data=Callback.StartMenu.my_account)
        stats = InlineKeyboardButton(text=LazyProxy('buttons-stats'),
                                     callback_data=Callback.StartMenu.stats)
        about = InlineKeyboardButton(text=LazyProxy('buttons-about'),
                                     callback_data=Callback.StartMenu.about)

        builder.add(choose_neuro, my_account, stats, about)
        builder.row(self.close(as_button=True))
        builder.adjust(1, 2, 1, 1)

        return builder.as_markup()

    async def favourite(self,
                        user_id: int,
                        page) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()
        
        status = {
            True: LazyProxy('messages-working').data,
            False: LazyProxy('messages-not_working').data
        }

        from ...database import database
        neuros = await database.get_favourites(user_id=user_id, 
                                               page=page,
                                               per_page=6)
        for neuro in neuros[0]:            
            neuro_info = await database.get_neuro(neuro)
            
            if neuro_info:
                text = LazyProxy(f'buttons-{neuro_info.code_name}').data + f" ({status[neuro_info.is_active]})"

                callback_data = Callback.Neuro(category=neuro_info.category,
                                           name=neuro_info.code_name,
                                           provider=neuro_info.provider).pack()
                builder.add(InlineKeyboardButton(text=text, callback_data=callback_data))
        
        builder.adjust(2, repeat=True)
            
        pagination = self._pagination(data_object=Callback.FavouritePagination,
                                      pages_count=neuros[1],
                                      current_page=page,
                                      user_id=user_id)
        
        builder.row(*pagination)

        builder.row(self.back(callback_data=Callback.StartMenu.choose_neuro,
                              as_button=True))
        return builder.as_markup()
    
    def whisper_modes(self):
        builder = InlineKeyboardBuilder()
        
        transcription = InlineKeyboardButton(text=LazyProxy('buttons-transcribe'),
                                            callback_data=Callback.Mode(type_=Task.TRANSCRIBE).pack())
        translation = InlineKeyboardButton(text=LazyProxy('buttons-translate'),
                                            callback_data=Callback.Mode(type_=Task.TRANSLATE).pack())

        builder.add(transcription, translation)
        builder.row(self.back(callback_data=Callback.Category(name=Category.AUDIO,
                                                              page=1).pack(), 
                              as_button=True))
        
        return builder.as_markup()