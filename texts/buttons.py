class ReplyButtons:
    neuro_choose = '🔥 Выбор нейросети'
    my_account = '👤 Мой аккаунт'
    stats = '✨ Статистика'
    faq = '❓ FAQ / Помощь'
    about = "💬 О сервисе"
    admin = "👨‍💻 Админ-панель"

    stop_chatting = '❌ Закончить диалог'

class InlineButtons:
    close = '❌ Закрыть'
    back = '⬅️ Назад'

    class NeuroCategories:
        text = '📝 Текст'
        image = '🖼 Изображения'
        audio = '🎵 Аудио'

    class Neuros:
        gpt = '💭 ChatGPT (GPT 3.5)'
        claude = '☁️ Claude AI'
        google = '📱 Google AI'
        llama = '🦙 LLaMA AI'
        mistral = '💻 Mistral AI (Medium)'
        gemini = '📚 Google Gemini Pro'
        stable = '🎨 StableDiffusionXL'
        playground = '🎮 Playground v2'
        enhance = '✨ EnhanceImage'
        midjourney = '📷 Midjourney V4'
        dalle3 = '🖼 DALL·E 3'
        sdv = '📹 StableDiffusion Video'
        whisper = '🎤 Whisper V3'
        bender = '🗣️ RachelVoice'

    class Mode:
        one_request = '🔥 Одиночный запрос'
        chat = '👥 Чат-бот'

    class Links:
        channel = '📢 Наш канал'
        api_dev = "🧑‍💻 Поставщик API"

    class AdminPanel:
        mailing = '📨 Рассылка'
        find_user = '🔍 Найти пользователя'
        change_neuro = '🔥 Сменить статус нейросети'

        maintenance = ['🔨 Включить техническое обслуживание', '🔨 Выключить техническое обслуживание']

        admins = ["🔥 Добавить администратора", "🧯 Снять администратора"]
        bans = ["🫣 Забанить пользователя", "🥰 Разбанить пользователя"]
    
    class Callback:
        close = 'close'
        back = 'back'

        class NeuroCategories:
            start = 'category_'
            back = 'category_back'
            text = 'category_text'
            image = 'category_image'
            audio = 'category_audio'

        class Neuros:
            start = 'neuro_'
            gpt= 'neuro_gpt'
            claude = 'neuro_claude'
            google = 'neuro_google'
            llama = 'neuro_llama'
            gemini = 'neuro_gemini'
            stable = 'neuro_stable'
            playground = 'neuro_playground'
            enhance = 'neuro_enhance'
            midjourney = 'neuro_midjourney'
            dalle3 = 'neuro_dalle3'
            sdv = 'neuro_sdv'
            whisper = 'neuro_whisper'
            bender = 'neuro_bender'
            mistral = 'neuro_mistral'
            switch = 'switch_'

        class Mode:
            start = 'mode_'
            one_request = 'mode_one_request'
            chat = 'mode_chat'

        class StartMenu:
            choose_neuro = 'choose_neuro'
            my_account = 'my_account'
            stats = 'stats'
            about = 'about'

        class AdminPanel:
            mailing = 'mailing'
            find_user = 'find_user'
            change_neuro = 'change_neuro'
            back = 'admin_back'
            ban='ban_'
            admin='admin_'
            maintenance='maintenance'
        
class AllNeuros:
    data = {
        InlineButtons.Neuros.gpt: InlineButtons.Callback.Neuros.gpt,
        InlineButtons.Neuros.claude: InlineButtons.Callback.Neuros.claude,
        InlineButtons.Neuros.google: InlineButtons.Callback.Neuros.google,
        InlineButtons.Neuros.llama: InlineButtons.Callback.Neuros.llama,
        InlineButtons.Neuros.mistral: InlineButtons.Callback.Neuros.mistral,
        InlineButtons.Neuros.gemini: InlineButtons.Callback.Neuros.gemini,
        InlineButtons.Neuros.stable: InlineButtons.Callback.Neuros.stable,
        InlineButtons.Neuros.playground: InlineButtons.Callback.Neuros.playground,
        InlineButtons.Neuros.enhance: InlineButtons.Callback.Neuros.enhance,
        InlineButtons.Neuros.midjourney: InlineButtons.Callback.Neuros.midjourney,
        InlineButtons.Neuros.sdv: InlineButtons.Callback.Neuros.sdv,
        InlineButtons.Neuros.dalle3: InlineButtons.Callback.Neuros.dalle3,
        InlineButtons.Neuros.whisper: InlineButtons.Callback.Neuros.whisper,
        InlineButtons.Neuros.bender: InlineButtons.Callback.Neuros.bender,
    }