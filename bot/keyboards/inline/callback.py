class Callback:
    close = 'close'
    again = 'again_'

    class Settings:
        back = "back_settings"
        set_language = "set_language"

    class Pagination:
        show_page = "show_page"
        unavailable_page = "unavailable_page"

    class Profile:
        back = "back_profile"

    class NeuroCategories:
        start = 'category_'
        back = 'category_back'
        text = 'category_text'
        image = 'category_image'
        audio = 'category_audio'
        admin = "cat_admin_"

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
        midjourneyv6 = 'neuro_midjourneyv6'
        juggernaut = 'neuro_juggernaut'
        dynavision = 'neuro_dynavision'
        animeart = 'neuro_animeart'
        dalle3 = 'neuro_dalle3'
        sdv = 'neuro_sdv'
        tencentmaker = 'neuro_tencentmaker'
        whisper = 'neuro_whisper'
        bender = 'neuro_bender'
        mistral = 'neuro_mistral'
        solar= 'neuro_solar'
        switch = 'switch_'

        vision_neuros = [juggernaut, dynavision, animeart]

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
        ban = 'ban_'
        admin = 'admin_'
        maintenance = 'maintenance'

    class Chat:
        autotrans = 'autotrans'

class Neuros:
    gpt = '💭 ChatGPT (GPT 3.5)'
    claude = '☁️ Claude AI'
    google = '📱 Google AI'
    llama = '🦙 LLaMA AI'
    mistral = '💻 Mistral AI (Medium)'
    solar = '🌤 Solar AI'
    gemini = '📚 Google Gemini Pro'
    stable = '🎨 StableDiffusionXL'
    playground = '🎮 Playground v2'
    enhance = '✨ EnhanceImage'
    midjourney = '📷 Midjourney V4'
    midjourneyv6 = '🔥 Midjourney V6'
    dalle3 = '🖼 DALL·E 3'
    tencentmaker = '🖌 TencentARC PhotomaMaker'
    juggernaut = "🦾 JuggernautXL V5"
    dynavision = "👁️ DynaVision XL"
    animeart = '🧝🏻‍♀️ Anime Art'
    sdv = '📹 StableDiffusion Video'
    whisper = '🎤 Whisper V3'
    bender = '🗣️ RachelVoice'

    neuro_names = ['gpt', 'claude', 'google',
                   'llama', 'gemini', 'stable',
                   'mistral', 'playground', 'enhance', 
                   'midjourney', 'dalle3', 'whisper', 
                   'bender', 'sdv', 'solar', 'tencentmaker',
                   'midjourneyv6', 'animeart', 'juggernaut',
                   'dynavision'
                   ]

class AllNeuros:
    data = {
        "text": {
            Neuros.gpt: Callback.Neuros.gpt,
            Neuros.claude: Callback.Neuros.claude,
            Neuros.google: Callback.Neuros.google,
            Neuros.llama: Callback.Neuros.llama,
            Neuros.mistral: Callback.Neuros.mistral,
            Neuros.solar: Callback.Neuros.solar,
            Neuros.gemini: Callback.Neuros.gemini
        },
        "image": {
            Neuros.stable: Callback.Neuros.stable,
            Neuros.playground: Callback.Neuros.playground,
            Neuros.midjourney: Callback.Neuros.midjourney,
            Neuros.midjourneyv6: Callback.Neuros.midjourneyv6,
            Neuros.enhance: Callback.Neuros.enhance,
            Neuros.sdv: Callback.Neuros.sdv,
            Neuros.dalle3: Callback.Neuros.dalle3,
            Neuros.tencentmaker: Callback.Neuros.tencentmaker,
            Neuros.juggernaut: Callback.Neuros.juggernaut,
            Neuros.dynavision: Callback.Neuros.dynavision,
            Neuros.animeart: Callback.Neuros.animeart
        },
        "audio": {
            Neuros.whisper: Callback.Neuros.whisper,
            Neuros.bender: Callback.Neuros.bender
        }
    }