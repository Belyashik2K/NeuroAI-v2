from ..config import Config

class MailingButtons:

    class Back:
        back_to_admin = '↪️ Назад'
        back_to_mailing = '↪️ Назад в меню рассылки'

    class Menu:
        start = '📩 Начать рассылку'
        view_message = '🖼 Предпросмотр'
        button = '📌 Кнопка под сообщением'
        text = '✍️ Текст'
        media = '📷 Медиа'
        disable_webpage_preview = '👀 Превью ссылки'
        reset = '🔄 Сбросить информацию о рассылке'

    class EditButton:
        button_text = '📌 Текст кнопки'
        button_link = '🔗 Ссылка кнопки'

    class StartMailing:
        sure = '✅ Уверен'

class MailingData:
    
    class Back:
        back_to_mailing = Config.mailing_button_data

    class Menu:
        start = 'mmstart'
        view_message = 'mmviewmessage'
        button = 'mmbutton'
        text = 'mmtext'
        media = 'mmmedia'
        disable_webpage_preview = 'mmdisablewebpagepreviewbutton'
        reset = 'mmreset'

    class EditButton:
        button_text = 'mmeditbuttontext'
        button_link = 'mmeditbuttonlink'

    class StartMailing:
        sure = 'mmstartmailingsure'