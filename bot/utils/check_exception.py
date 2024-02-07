import logging

from aiogram.enums import ParseMode

from aiogram_i18n import LazyProxy


class ExceptionChecker:

    @staticmethod
    def check_exception(exception: str) -> dict:
        logging.error(exception)
        data = dict()

        if "end of the entity starting" in exception:
            data['text'] = LazyProxy('errors-error_with_entities').data
            data['parse_mode'] = ParseMode.MARKDOWN
        elif "MESSAGE_TOO_LONG" in exception:
            data['text'] = LazyProxy('errors-error_with_lenght').data
        else:
            data['text'] = LazyProxy('errors-unknown_error').data
        return data
