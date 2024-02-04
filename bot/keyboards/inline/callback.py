from aiogram.filters.callback_data import CallbackData

from ...enums import *

class Callback:
    close = 'close'

    class Pagination:
        show_page = "show_page"
        unavailable_page = "unavailable_page"

    class StartMenu:
        choose_neuro = 'choose_neuro'
        my_account = 'my_account'
        stats = 'stats'
        about = 'about'
        admin = 'admin'

    class Settings:
        set_language = "set_language"

    class AdminPanel:
        mailing = 'mailing'
        find_user = 'find_user'
        change_neuro = 'change_neuro'
        maintenance = 'maintenance'

    class Chat: # TODO: remove
        autotrans = 'autotrans'

    # Factories for CallbackData

    class Category(CallbackData, prefix="category", sep="_"):
        name: str
        page: int

    class Neuro(CallbackData, prefix="neuro"):
        provider: str
        category: str
        name: str

    class Mode(CallbackData, prefix="mode"):
        type_: str

    class AdminCategory(CallbackData, prefix="admin_category"):
        name: str
        page: int

    class Switch(CallbackData, prefix="switch"):
        neuro_name: str

    class BanUser(CallbackData, prefix="ban"):
        user_id: int

    class AdminUser(CallbackData, prefix="admin"):
        user_id: int

class NeuroInfo:
    not_working = [Neuro.ENHANCE, Neuro.DALLE3, Neuro.BENDER]
    neuros_alph = {
        Provider.FUTUREFORGE: {
            Category.TEXT: [Neuro.CHATGPT, Neuro.CLAUDE, Neuro.GOOGLE, 
                            Neuro.LLAMA, Neuro.MISTRAL, Neuro.SOLAR, 
                            Neuro.GEMINI],
            Category.IMAGE: [Neuro.SDXL, Neuro.PLAYGROUND, 
                             Neuro.MIDJOURNEYV4, Neuro.MIDJOURNEYV6,
                             Neuro.ENHANCE, Neuro.VIDEODIFFUSION,
                             Neuro.DALLE3, Neuro.TENCENTMAKER],
            Category.AUDIO: [Neuro.WHISPER, Neuro.BENDER],
        },
        Provider.VISIONCRAFT: {
            Category.TEXT: [Neuro.CAPYBARA, Neuro.ZEPHYR,
                            Neuro.OPENCHAT, Neuro.MYTHOMIST,
                            Neuro.CINEMATIKA, Neuro.RWKV5WORLD,
                            Neuro.RWKV5AITOWN],
            Category.IMAGE: [Neuro.GOUFENG, Neuro.ABSOLUTEREALITY, Neuro.AMIREAL,
                             Neuro.ANALOGDIFFUSION, Neuro.ANYTHING,
                             Neuro.ABYSSORANGEMIX, Neuro.BLAZINGDRIVE,
                             Neuro.CETUSMIX, Neuro.CHILDRENSSTORIES3D,
                             Neuro.CHILDRENSSTORIESSEMI, Neuro.CHILDRENSSTORIESTOON,
                             Neuro.COUNTERFEIT, Neuro.CUTEYUKIMIX,
                             Neuro.CYBERREALISTIC, Neuro.DALCEFO,
                             Neuro.DELIBERATE2, Neuro.DREAMLIKEANIME,
                             Neuro.DREAMLIKEDIFFUSION, Neuro.DREAMLIKEPHOTOREAL,
                             Neuro.DREAMSHAPER, Neuro.EOR,
                             Neuro.EIMISANIMEDIFFUSION, Neuro.ELLDRETHS,
                             Neuro.EPICREALISM, Neuro.CANTBELIEVE,
                             Neuro.JUGGERNAUTAFTERMATH, Neuro.LOFI,
                             Neuro.LYRIEL, Neuro.MAJICMIXREALISTIC,
                             Neuro.MECHAMIX, Neuro.NEVERENDINGDREAM,
                             Neuro.PASTELMIXSTYLIZED, Neuro.PORTRAITPLUS,
                             Neuro.PROTOGEN, Neuro.REALISTICVISION,
                             Neuro.REDSHIFTDIFFUSION, Neuro.REVANIMATED,
                             Neuro.RUNDIFFUSIONFX, Neuro.SHONINSBEAUTIFUL,
                             Neuro.THEALLYSMIX, Neuro.TIMELESS, Neuro.TOONYOU]
                             }
    }