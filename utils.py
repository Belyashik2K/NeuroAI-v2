from config import Config

class Utils:

    def get_file_url(file_path: str) -> str:
        return "https://api.telegram.org/file/bot{}/{}".format(Config.BOT_TOKEN, file_path)