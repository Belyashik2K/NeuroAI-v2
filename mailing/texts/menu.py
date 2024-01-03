class MenuTexts:

    mailing_menu_types = {
        
        "no_media": """📣 <b>Рассылка</b>

👤 <b>Всего пользователей в боте</b> >>> <code>{}</code>

📈 <b>Живых/мёртвых пользователей в последней рассылке</b> >>> <code>{}</code>/<code>{}</code>

ℹ️ <b>Информация о рассылке</b>

<b>Тип рассылки</b> >>> <code>{}</code>

<b>Текст</b> >>> {}
<b>Медиа (ID Telegram)</b> >>> <code>{}</code>
<b>Кнопка под сообщением</b>
├ <b>Текст кнопки</b> >>> <code>{}</code>
└ <b>Ссылка кнопки</b> >>> <code>{}</code>
<b>Отключить превью ссылки (disable_webpage_preview)</b> >>> <code>{}</code>

<i>by <a href="https://t.me/Belyashik2K">Belyashik2K</a> with ❤️</i>""",

    "with_media": """📣 <b>Рассылка</b>

👤 <b>Всего пользователей в боте</b> >>> <code>{}</code>

📈 <b>Живых/мёртвых пользователей в последней рассылке</b> >>> <code>{}</code>/<code>{}</code>

ℹ️ <b>Информация о рассылке</b>

<b>Тип рассылки</b> >>> <code>{}</code>

<b>Текст</b> >>> {}
<b>Медиа (ID Telegram)</b> >>> <code>{}</code>
<b>Кнопка под сообщением</b>
├ <b>Текст кнопки</b> >>> <code>{}</code>
└ <b>Ссылка кнопки</b> >>> <code>{}</code>

<i>by <a href="https://t.me/Belyashik2K">Belyashik2K</a> with ❤️</i>""",

    "video_note": """📣 <b>Рассылка</b>

👤 <b>Всего пользователей в боте</b> >>> <code>{}</code>

📈 <b>Живых/мёртвых пользователей в последней рассылке</b> >>> <code>{}</code>/<code>{}</code>

ℹ️ <b>Информация о рассылке</b>

<b>Тип рассылки</b> >>> <code>{}</code>

<b>Медиа (ID Telegram)</b> >>> <code>{}</code>
<b>Кнопка под сообщением</b>
├ <b>Текст кнопки</b> >>> <code>{}</code>
└ <b>Ссылка кнопки</b> >>> <code>{}</code>

<i>by <a href="https://t.me/Belyashik2K">Belyashik2K</a> with ❤️</i>"""
    }

    mailing_sure = """📣 <b>Рассылка</b>
        
Вы уверены, что хотите начать рассылку на <code>{}</code> пользователей?

⚠️ <i>Перед началом рассылки обязательно проверьте правильность рассылаемого сообщения, нажав на кнопку <code>🖼 Предпросмотр</code> в меню рассылки!</i>"""

    mailing_start = """📨 <b>Рассылка успешно запущена!</b>
    
🕔 <i>Статистика обновляется в реальном времени</i>
├ <b>Удачно отправленных сообщений пользователям</b> >>> <code>{}</code>
└ <b>Неудачно отправленных сообщений пользователям</b> >>> <code>{}</code>"""

    mailing_end = """👌 <b>Рассылка завершена!</b>
    
✉️ <i>Статистика проведённой рассылки</i>
├ <b>Удачно отправлено сообщений пользователям</b> >>> <code>{}</code>
└ <b>Неудачно отправлено сообщений пользователям</b> >>> <code>{}</code>"""

    mailing_text = """📣 <b>Рассылка</b>
    
<b>Введите текст для рассылки</b>

⚠️ <i>Если в рассылке используется фотография, прикреплённая как медиа, то ограничение символов >>> <code>1024</code>. Если фотографии нет или она прикреплена как превью, то ограничение символов >>> <code>4096</code></i>"""

    mailing_media = """📣 <b>Рассылка</b>
    
<b>Пришлите медиа для рассылки</b>

⚠️ <i>Поддерживаемые типы медиафайлов</i>
├ <i>Фотография</i>
├ <i>Видеозапись</i>
├ <i>Аудиозапись</i>
├ <i>Голосовое сообщение</i>
├ <i>Видеосообщение</i>
├ <i>GIF-анимация</i>
└ <i>Документ</i>"""

    mailing_button_text = """📣 <b>Рассылка</b>
    
<b>Введите текст для кнопки под сообщением рассылки</b>"""

    mailing_button_link = """📣 <b>Рассылка</b>
    
<b>Пришлите ссылку для кнопки под сообщением рассылки</b>

⚠️ <i>Ссылка в формате <code>https://example.com/test_page</code></i>
<i>Ссылки в другом формате не будут обработаны.</i>"""

    mailing_button_menu = """📣 <b>Рассылка</b>
    
<b>Что нужно изменить в кнопке под сообщением?</b>

⚠️ <i>Если устанавливаете текст кнопки, то обязательно установите и ссылку, иначе кнопка отображаться не будет!</i>"""

    done = "👌 Успешно"

    mailing_not_set = "Перед началом рассылки необходимо настроить рассылку!"