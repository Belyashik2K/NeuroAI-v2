from ..config import config

class Links:

    @staticmethod
    def get_file_url(file_path: str) -> str:
        return "https://api.telegram.org/file/bot{}/{}".format(config.BOT_TOKEN.get_secret_value(), file_path)