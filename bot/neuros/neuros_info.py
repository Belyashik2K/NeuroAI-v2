from ..enums import Neuro, Provider, Category


class NeuroInfo:
    not_working = [Neuro.ENHANCE, Neuro.DALLE3, Neuro.BENDER,
                   Neuro.MIDJOURNEYV6, Neuro.ANIMEART, Neuro.DYNAVISION, 
                   Neuro.JUGGERNAUT, Neuro.SDXL]
    neuros_alph = {
        Provider.FUTUREFORGE: {
            Category.TEXT: [Neuro.CHATGPT, Neuro.CLAUDE, Neuro.GOOGLE,
                            Neuro.LLAMA, Neuro.MISTRAL, Neuro.SOLAR,
                            Neuro.GEMINI],
            Category.IMAGE: [Neuro.PLAYGROUND,
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
                             Neuro.THEALLYSMIX, Neuro.TIMELESS, Neuro.TOONYOU,
                             ],
        }
    }
