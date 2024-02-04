from aiogram.filters.callback_data import CallbackData

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

    class Neuro(CallbackData, prefix="neuro"):
        provider: str
        category: str
        name: str

    class Mode(CallbackData, prefix="mode"):
        type_: str

    class AdminCategory(CallbackData, prefix="admin_category"):
        name: str

    class Switch(CallbackData, prefix="switch"):
        neuro_name: str

    class BanUser(CallbackData, prefix="ban"):
        user_id: int

    class AdminUser(CallbackData, prefix="admin"):
        user_id: int

class AllNeuros:
    not_working = ['enhance', 'dalle3', 'bender']

    data_1 = {
        "futureforge": {
            "text": ['gpt', 'claude', 'google', 'llama', 'gemini', 'mistral', 'solar'],
            "image": ['playground', 'enhance', 'midjourney', 'dalle3', 'sdv', 'stable', 'tencentmaker', 'midjourneyv6'],
            "audio": ['whisper', 'bender'],
        },
        "visioncraft": {
            "text": ['capybara'],
            "image": ['juggernaut', 'dynavision', 'animeart']
        }
    }