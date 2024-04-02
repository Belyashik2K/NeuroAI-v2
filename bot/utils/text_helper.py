from aiogram_i18n import LazyProxy

from ..enums import Category

class TextHelper:
    
    @classmethod
    def html_screening(cls,
                       text: str) -> str:
        return text.replace("<", "&lt;"
                    ).replace(">", "&gt;")
    
    @classmethod
    def prepaire_text(cls,
                      text: str,
                      request_category: str = Category.IMAGE) -> str:
        if request_category == Category.IMAGE:
            if len(text) >= 1000:
                return LazyProxy('errors-too_long_prompt').data
            return cls.html_screening(text=text)