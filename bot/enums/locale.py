from typing import Optional


class Locale:
    EN = "en"
    RU = "ru"
    DE = "de"
    UA = "ua"
    CN = 'cn'
    HE = 'he'
    DEFAULT = EN

    DATA_LIST = [EN, RU, DE, UA, CN, HE]

    class Buttons:
        RU = "🇷🇺 Русский"
        EN = "🇬🇧 English"
        DE = "🇩🇪 Deutsch"
        UA = "🇺🇦 Українська"
        CN = '🇨🇳 中文'
        HE = '🇮🇱 עברית'

    @classmethod
    def resolve(cls, locale: Optional[str]) -> str:
        if not locale or locale not in list(cls.__dict__.values()):
            return cls.DEFAULT
        return locale
