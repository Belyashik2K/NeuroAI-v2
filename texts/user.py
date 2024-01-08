class UserTexts:
    start_command = """🙋 Добро пожаловать в мир нейросетей, {}!
    
Я — {}, обновленная версия бота NeuroAI, которая поможет тебе удобно и эффективно работать с нейросетями!

<b>Мои преимущества:</b>
— Отвечаю на твои вопросы в формате <b>диалога</b> или <b>одиночного сообщения</b>
— Генерирую <b>фотографии</b> по заданному запросу
— Генерирую аудиофайлы по заданному запросу и перевожу их
— <b>Абсолютно бесплатен</b> и работаю на основе <a href="https://api.futureforge.dev/docs">API FutureForge</a>
— Имею <b>открытый</b> исходный код, который ты можешь найти в моем репозитории на <a href="https://github.com/Belyashik2K/NeuroAI-v2">GitHub</a>

🆘 Техническая поддержка >>> {}
🥀 Сотрудничество >>> {}"""

    class AboutUs:
        about_us = """💬 <b>О сервисе</b>
<i>Основная информация и ссылки</i>

🆘 Техническая поддержка: {support}
🥀 Cотрудничество: {ads}

🤔 <b>Работоспосособность нейросетей</b>
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
└ RachelVoice: <code>{bender}</code>"""

        working = "Работает"
        not_working = "На техническом обслуживании"

    class Stats:
        stats = """✨ <b>Статистика</b>
<i>На {}.{}.{}</i>

👤 Пользователей: <code>{}</code>
🔎 Генераций пользователями бота: <code>{}</code>"""

    class Profile:
        user = """👤 <b>Мой аккаунт</b>
<i>Основная информация</i>

👤 Ваше имя: {}
💬 Ваш NeuroID: <code>{}</code>
⚙️ Количество совершённых генераций: <code>{}</code>

📅 Дата регистрации: <code>{}</code>"""

    class Neuros:
        choose_neuro_category = """❓ <b>Выберите категорию нейросети</b>
        
📝 <code>Текст</code> — нейросети, которые генерируют текст.
<i>Список нейросетей:</i>
├ <code>💭 ChatGPT (GPT 3.5)</code>
├ <code>☁️ Claude AI</code>
├ <code>📱 Google AI</code>
├ <code>🦙 LLaMA AI</code>
├ <code>💻 Mistral AI (Medium)</code>
└ <code>📚 Google Gemini Pro</code>

🖼 <code>Изображения</code> — нейросети, которые генерируют изображения.
<i>Список нейросетей:</i>
├ <code>🎨 StableDiffusionXL</code>
├ <code>🎮 Playground v2</code>
├ <code>✨ EnhanceImage</code>
├ <code>📷 Midjourney V4</code>
├ <code>📹 StableDiffusion Video</code>
└ <code>🖼 DALL·E 3</code>

🎵 <code>Аудио</code> — нейросети, которые генерируют аудио.
<i>Список нейросетей:</i>
├ <code>🎤 Whisper V3</code>
└ <code>🗣️ RachelVoice</code>"""

        choose_neuro = """❓ <b>Выберите нейросеть</b>\n\n"""

        category_text = """<code>💭 ChatGPT (GPT 3.5)</code> — одна из самых стабильных нейросетей для генерации текста. Она способна генерировать тексты, писать код, отвечать на вопросы и многое другое. Может обрабатывать ссылки на сайты.

<code>☁️ Claude AI</code> —  ассистент ИИ нового поколения, основанный на исследованиях Anthropic по обучению полезным, честным и безвредным системам ИИ. Claude способен выполнять широкий спектр задач по обработке разговоров и текста, сохраняя при этом высокую степень надежности и предсказуемости. Работает преимущественно с английским языком.

<code>📱 Google AI</code> — нейросеть от Google, которая способна генерировать тексты, преимущественно на английском языке.

<code>🦙 LLaMA AI</code> — большая языковая модель (LLM), выпущенная Meta AI в феврале 2023 года. Были обучены модели различных размеров в диапазоне от 7 до 65 миллиардов весов.

<code>💻 Mistral AI (Medium)</code> — большая языковая модель машинного обучения с семью миллиардами параметров. Ответы на уровне ChatGPT, но с более высоким качеством. Работает преимущественно с английским языком.

<code>📚 Google Gemini Pro</code> — одна из наиболее продвинутых нейросетей, выпущенная компанией Google. Она способна генерировать тексты, смотреть на изображения и отвечать на вопросы как на английском, так и на русском языке.
В режиме <code>👥 Чат-бот</code> может анализировать фотографии."""

        category_image = """<code>🎨 StableDiffusionXL</code> — нейросеть, которая способна генерировать изображения по заданному запросу. Даёт четкие и качественные изображения при использовании хорошего промпта.

<code>🎮 Playground v2</code> — одна из лучших нейросетей для генерации изображений. Способная генерировать изображения по заданному запросу.

<code>✨ EnhanceImage</code> — нейросеть, которая способна улучшать качество изображений.

<code>📷 Midjourney V4</code> — нейросеть, которая способна генерировать изображения по заданному запросу. Даёт четкие и качественные изображения при использовании хорошего промпта.

<code>📹 StableDiffusion Video</code> — нейросеть, которая способна генерировать видео по полученной фотографии.

<code>🖼 DALL·E 3</code> — одна из наиболее продвинутых нейросетей для генерации изображений от компании OpenAI."""

        category_audio = """<code>🎤 Whisper V3</code> — нейросеть, которая способна переводить аудиофайл в текст.

<code>🗣 RachelVoice</code> — нейросеть, которая способна генерировать аудиофайлы по заданному тексту."""

        choose_mode = """🤖 <i>Выбранная нейросеть:</i> <code>{}</code>

❓ <b>Выберите режим работы</b>
    
🔥 <code>Одиночный запрос</code> — бот сгенерирует один ответ на ваш запрос и отправит его вам.

👥 <code>Чат-бот</code> — бот будет отвечать на ваши сообщения, пока вы не завершите диалог."""

        header = """🤖 <i>Выбранная нейросеть:</i> <code>{}</code>
<i>❓ Выбранный режим:</i> <code>{}</code>

"""
        one_request_mode = header + """<b>Введите ваш запрос</b> или нажмите кнопку <code>⬅️ Назад</code> для отмены запроса."""

        one_request_processing = header + """<b>Ваш запрос:</b> <code>{}</code>

😌 <i>Обработка запроса, пожалуйста, подождите...</i>"""

        one_request_result = """🤖 _Выбранная нейросеть:_ `{}`
❓ _Выбранный режим:_ `{}`

_Ваш запрос:_ `{}`
_Ответ нейросети:_ {}
"""

        chat_mode = header + """🎉 <b>Диалог с ботом начат.</b> Для завершения диалога нажмите кнопку <code>❌ Закончить диалог</code>."""

        chatting = "😌 Один момент, пожалуйста, я обрабатываю ваш запрос..."

        awaiting_chat_code = """🔄 Создаю новый диалог, пожалуйста, подождите..."""

        answer = "🤖 {}"

        stop_chatting = """👋 Диалог с ботом завершён, возвращаю Вас в главное меню."""

        start_gen_image = """🤖 <i>Выбранная нейросеть:</i> <code>{}</code>
        
<b>Введите ваш запрос</b> или нажмите кнопку <code>⬅️ Назад</code> для отмены запроса.

<b>Пишите на английском языке и обязательно ознакомьтесь с памяткой по созданию запросов → <a href="https://telegra.ph/Pamyatka-kak-sostavit-idealnyj-zapros-12-26">тык</a></b>"""

        gen_image_processing = """🤖 <i>Выбранная нейросеть:</i> <code>{}</code>

<b>Ваш запрос:</b> <code>{}</code>

😌 <i>Обработка запроса, пожалуйста, подождите...</i>"""

        gen_image_result = """🤖 _Выбранная нейросеть:_ `{}`

_Ваш запрос:_ `{}`"""

        what_on_image = """Что на фотографии?"""

        image_link = "\n\nСсылка на фотографию >>> {}"

        enchance_image = """🤖 <i>Выбранная нейросеть:</i> <code>{}</code>

<b>Отправьте фотографию, которую нужно улучшить</b> или нажмите кнопку <code>⬅️ Назад</code> для отмены запроса."""

        enchance_image_processing = """🤖 <i>Выбранная нейросеть:</i> <code>{}</code>

😌 <i>Обработка запроса, пожалуйста, подождите...</i>"""

        enchance_image_result = """🤖 _Выбранная нейросеть:_ `{}`"""

        bender_voice = """🤖 <i>Выбранная нейросеть:</i> <code>{}</code>

<b>Введите текст, который нужно озвучить</b> или нажмите кнопку <code>⬅️ Назад</code> для отмены запроса."""

        bender_voice_processing = """🤖 <i>Выбранная нейросеть:</i> <code>{}</code>

<b>Ваш запрос:</b> <code>{}</code>

😌 <i>Обработка запроса, пожалуйста, подождите...</i>"""

        bender_voice_result = """🤖 _Выбранная нейросеть:_ `{}`

_Ваш запрос:_ `{}`

⚠️ __Внимание!__ Запрос был огранничен до 330 символов."""

        whisper_voice = """🤖 <i>Выбранная нейросеть:</i> <code>{}</code>

<b>Отправьте аудиофайл, который нужно перевести в текст</b> или нажмите кнопку <code>⬅️ Назад</code> для отмены запроса."""

        whisper_voice_processing = """🤖 <i>Выбранная нейросеть:</i> <code>{}</code>

😌 <i>Обработка запроса, пожалуйста, подождите...</i>"""

        whisper_voice_result = """🤖 _Выбранная нейросеть:_ `{}`
        
_Ответ нейросети:_ {}"""

        sdv_video = """🤖 <i>Выбранная нейросеть:</i> <code>{}</code>

<b>Отправьте фотографию, которую нужно анимировать</b> или нажмите кнопку <code>⬅️ Назад</code> для отмены запроса."""

        sdv_video_processing = """🤖 <i>Выбранная нейросеть:</i> <code>{}</code>

😌 <i>Обработка запроса, пожалуйста, подождите...</i>"""

        sdv_video_result = """🤖 _Выбранная нейросеть:_ `{}`"""