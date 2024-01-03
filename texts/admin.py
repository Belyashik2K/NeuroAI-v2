class AdminTexts:
    admin_menu = """👨‍💻 <b>Админ-панель</b>"""

    error = """😣 Произошла <b>ошибка</b>
    
👤 Информация о пользователе
├ ID >>> <code>{user_id}</code>
└ Упоминание >>> {mention}

📝 Информация об ошибке
└ Ошибка >>> <code>{exception}</code>
"""

    find_user = """🔍 <b>Поиск пользователя</b>
    
Введите NeuroID пользователя, которого хотите найти."""

    user_info = """👤 <b>Информация о пользователе</b>
<i>Основная информация</i>

👤 Имя >>> {}
💬 NeuroID >>> <code>{}</code>
⚙️ Количество совершённых генераций >>> <code>{}</code>

📅 Дата регистрации >>> <code>{}</code>"""

    choose_neuro = """❓ <b>Выберите нейросеть для смены статуса</b>"""

    success = """✅ Статус нейросети успешно изменён."""

    success_edit = """✅ Статус пользователя успешно изменен."""

    success_maintenance = """✅ Статус бота успешно изменён."""

    new_user = """🎉 <b>Новый пользователь в боте!</b>
    
👤 Пользователь >>> <a href="tg://user?id={user_id}">{full_name}</a>
💬 NeuroID >>> <code>{neuro_id}</code>"""

    neuro_statuses = """<b>🔥 Сменить статус нейросети</b>

Нейросети для генерации текста:
├ ChatGPT: <code>{gpt}</code>
├ Claude AI: <code>{claude}</code>
├ Google AI: <code>{google}</code>
├ LLaMA AI: <code>{llama}</code>
├ Mistral AI (Medium): <code>{mistral}</code>
└ Google Gemini Pro: <code>{gemini}</code>

Нейросети для генерации и обработки изображений:
├ StableDiffusionXL: <code>{stable}</code>
├ Playground v2: <code>{playground}</code>
├ EnhanceImage: <code>{enhance}</code>
├ Midjourney V4: <code>{midjourney}</code>
├ StableDiffusion Video: <code>{sdv}</code>
└ DALL·E 3: <code>{dalle3}</code>

Нейросети для работы с аудио:
├ Whisper V3: <code>{whisper}</code>
└ RachelVoice: <code>{bender}</code>
"""