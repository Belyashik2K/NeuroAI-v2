from ..enums import Neuro, Provider, Category


class NeuroInfo:
    not_working = [Neuro.BENDER,
                   Neuro.PLAYGROUND,
                   Neuro.MIDJOURNEYV6,
                   Neuro.VIDEODIFFUSION, Neuro.MIDJOURNEYV4,
                   Neuro.TENCENTMAKER, Neuro.GOOGLE,
                   Neuro.LLAMA, Neuro.MISTRAL, Neuro.SOLAR,
                   Neuro.SONNET, Neuro.OPUS]
    neuros_alph = {
        Provider.FUTUREFORGE: {
            Category.TEXT: [Neuro.GOOGLE,
                            Neuro.LLAMA, Neuro.MISTRAL, Neuro.SOLAR,
                            Neuro.SONNET, Neuro.OPUS],
            Category.IMAGE: [Neuro.PLAYGROUND,
                             Neuro.MIDJOURNEYV6,
                             Neuro.VIDEODIFFUSION,Neuro.MIDJOURNEYV4,
                             Neuro.TENCENTMAKER],
            Category.AUDIO: [Neuro.BENDER],
        },
        Provider.VISIONCRAFT: {
            Category.TEXT: [Neuro.LZLV, Neuro.PYGMALION, 
                            Neuro.AIRBOROS, Neuro.DOLPHIN, Neuro.GEMMA,
                            Neuro.LLAVA, Neuro.GEMINI, Neuro.GPT4,
                            Neuro.CHATGPT, Neuro.CLAUDE],
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
                             Neuro.ENHANCE, Neuro.SDXL, Neuro.JUGGERNAUT,
                             Neuro.DYNAVISION, Neuro.ANIMEART, Neuro.CASCADE,
                             Neuro.T2G, Neuro.I2I, Neuro.DALLE3],
            Category.AUDIO: [Neuro.WHISPER],
        }
    }
