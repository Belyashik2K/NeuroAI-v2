```Start```

messages-start = 🙋 Привет, { $name }!
    
    <b>Для продолжения работы с ботом, пожалуйста, выбери один из языков ниже 👇</b>

    ⚠️ <i>После выбора языка, ты сможешь изменить его в разделе</i> <code>👤 Мой аккаунт</code>

messages-info = 🙋 Добро пожаловать в мир нейросетей, { $name }!
    
    Я — { $self }, обновленная версия бота NeuroAI, которая поможет тебе удобно и эффективно работать с нейросетями!

    <b>Мои преимущества:</b>
    — Отвечаю на твои вопросы в формате <b>диалога</b> или <b>одиночного сообщения</b>
    — Генерирую <b>фотографии</b> по заданному запросу
    — Генерирую аудиофайлы по заданному запросу и перевожу их
    — <b>Абсолютно бесплатен</b> и работаю на основе <a href="https://api.futureforge.dev/docs">API FutureForge</a>
    — Имею <b>открытый</b> исходный код, который ты можешь найти в моем репозитории на <a href="https://github.com/Belyashik2K/NeuroAI-v2">GitHub</a>

    🆘 Техническая поддержка >>> { $technical_support }
    🥀 Сотрудничество >>> { $ads }

```Set language```

messages-choose_language = 🌐 <b>Сменить язык</b>

messages-lang_set = 🎉 Язык успешно изменен!

```Profile info```

messages-my_profile = 👤 <b>Мой аккаунт</b>
    <i>Основная информация</i>

    👤 Имя >>> { $name }
    💬 NeuroID >>> <code>{ $neuro_id }</code>
    ⚙️ Количество совершённых генераций >>> <code>{ $request_counter }</code>

    📅 Дата регистрации >>> <code>{ $join_date }</code>

```Stats```

messages-stats = ✨ <b>Статистика</b>
    <i>На { $date }</i>

    👤 Пользователей: <code>{ $users_count }</code>
    🔎 Генераций пользователями бота: <code>{ $requests_count }</code>

```About + Neuro statuses```

messages-about = 💬 <b>О сервисе</b>
    <i>Основная информация и ссылки</i>

    🆘 Техническая поддержка: { $support }
    🥀 Cотрудничество: { $ads }

    🤔 <b>Статусы нейросетей</b>
    Нейросети для генерации текста:
    ├ ChatGPT: <code>{ $gpt }</code>
    ├ Claude AI: <code>{ $claude }</code>
    ├ Google AI: <code>{ $google }</code>
    ├ LLaMA AI: <code>{ $llama }</code>
    ├ Mistral AI (Medium): <code>{ $mistral }</code>
    ├ Solar AI: <code>{ $solar }</code>
    └ Google Gemini Pro: <code>{ $gemini }</code>

    Нейросети для генерации и обработки изображений:
    ├ StableDiffusionXL: <code>{ $stable }</code>
    ├ Playground v2: <code>{ $playground }</code>
    ├ EnhanceImage: <code>{ $enhance }</code>
    ├ Midjourney V4: <code>{ $midjourney }</code>
    ├ Midjourney V6: <code>{ $midjourneyv6 }</code>
    ├ StableDiffusion Video: <code>{ $sdv }</code>
    ├ DALL·E 3: <code>{ $dalle3 }</code>
    └ TencentARC PhotoMaker: <code>{ $tencentmaker }</code>

    Нейросети для работы с аудио:
    ├ Whisper V3: <code>{ $whisper }</code>
    └ RachelVoice: <code>{ $bender }</code>

messages-working = Работает

messages-not_working = На техническом обслуживании

```Neuro categories```

messages-choose_neuro_category = <b>🔥 Выбор нейросети</b>
    ❓ <i>Выберите категорию нейросети</i>
        
    📝 <code>Текст</code> — нейросети, которые генерируют текст.
    <i>Список нейросетей:</i>
    ├ <code>💭 ChatGPT (GPT 3.5)</code>
    ├ <code>☁️ Claude AI</code>
    ├ <code>📱 Google AI</code>
    ├ <code>🦙 LLaMA AI</code>
    ├ <code>💻 Mistral AI (Medium)</code>
    ├ <code>🌤 Solar AI</code>
    └ <code>📚 Google Gemini Pro</code>

    🖼 <code>Изображения</code> — нейросети, которые генерируют изображения.
    <i>Список нейросетей:</i>
    ├ <code>🎨 StableDiffusionXL</code>
    ├ <code>🎮 Playground v2</code>
    ├ <code>✨ EnhanceImage</code>
    ├ <code>📷 Midjourney V4</code>
    ├ <code>🔥 Midjourney V6</code>
    ├ <code>📹 StableDiffusion Video</code>
    ├ <code>🖼 DALL·E 3</code>
    └ <code>🖌 TencentARC PhotoMaker</code>

    🎵 <code>Аудио</code> — нейросети, которые генерируют аудио.
    <i>Список нейросетей:</i>
    ├ <code>🎤 Whisper V3</code>
    └ <code>🗣️ RachelVoice</code>

```Neuro choose```

messages-choose_neuro = ❓ <b>Выберите нейросеть</b>

messages-category_text = <code>💭 ChatGPT (GPT 3.5)</code> — одна из самых стабильных нейросетей для генерации текста. Она способна генерировать тексты, писать код, отвечать на вопросы и многое другое. Может обрабатывать ссылки на сайты.

    <code>☁️ Claude AI</code> —  ассистент ИИ нового поколения, основанный на исследованиях Anthropic по обучению полезным, честным и безвредным системам ИИ. Claude способен выполнять широкий спектр задач по обработке разговоров и текста, сохраняя при этом высокую степень надежности и предсказуемости. Работает преимущественно с английским языком.

    <code>📱 Google AI</code> — нейросеть от Google, которая способна генерировать тексты, преимущественно на английском языке.

    <code>🦙 LLaMA AI</code> — большая языковая модель (LLM), выпущенная Meta AI в феврале 2023 года. Были обучены модели различных размеров в диапазоне от 7 до 65 миллиардов весов.

    <code>💻 Mistral AI (Medium)</code> — большая языковая модель машинного обучения с семью миллиардами параметров. Ответы на уровне ChatGPT, но с более высоким качеством. Работает преимущественно с английским языком.

    <code>🌤 Solar AI</code> - модель от компании Upstage занимает лидирующие позиции в рейтинге HuggingFace Open LLM и представляет собой улучшенную версию модели LLaMA 2.

    <code>📚 Google Gemini Pro</code> — одна из наиболее продвинутых нейросетей, выпущенная компанией Google. Она способна генерировать тексты, смотреть на изображения и отвечать на вопросы как на английском, так и на русском языке.

messages-category_image = <code>🎨 StableDiffusionXL</code> — нейросеть, которая способна генерировать изображения по заданному запросу. Даёт четкие и качественные изображения при использовании хорошего промпта.

    <code>🎮 Playground v2</code> — одна из лучших нейросетей для генерации изображений. Способная генерировать изображения по заданному запросу.

    <code>📷 Midjourney V4</code> — нейросеть, которая способна генерировать изображения по заданному запросу. Даёт четкие и качественные изображения при использовании хорошего промпта.

    <code>🔥 Midjourney V6</code> — лучшая нейросеть для генерации изображений на данный момент. Улучшенная версия <code>📷 Midjourney V4</code>

    <code>✨ EnhanceImage</code> — нейросеть, которая способна улучшать качество изображений.

    <code>📹 StableDiffusion Video</code> — нейросеть, которая способна генерировать видео по полученной фотографии.

    <code>🖼 DALL·E 3</code> — одна из наиболее продвинутых нейросетей для генерации изображений от компании OpenAI.

    <code>🖌 TencentARC PhotoMaker</code> —  нейросеть, которая способна сгенерировать любое изображение с любым лицом по заданному запросу. Фильтр NSFW отсутствует.

messages-category_audio = <code>🎤 Whisper V3</code> — нейросеть, которая способна переводить аудиофайл в текст.

    <code>🗣 RachelVoice</code> — нейросеть, которая способна генерировать аудиофайлы по заданному тексту.

messages-mode = 🤖 <i>Выбранная нейросеть:</i> <code>{ $neuro }</code>

    ❓ <b>Выберите режим работы</b>
        
    🔥 <code>Одиночный запрос</code> — бот сгенерирует один ответ на ваш запрос и отправит его вам.

    👥 <code>Чат-бот</code> — бот будет отвечать на ваши сообщения, пока вы не завершите диалог.

messages-header = 🤖 <i>Выбранная нейросеть:</i> <code>{ $neuro }</code>
    <i>❓ Выбранный режим:</i> <code>{ $mode }</code>

messages-one_request_mode = <b>Введите ваш запрос</b> или нажмите кнопку <code>⬅️ Назад</code> для отмены запроса.

messages-start_gen_image = 🤖 <i>Выбранная нейросеть:</i> <code>{ $neuro }</code>
        
    <b>Введите ваш запрос</b> или нажмите кнопку <code>⬅️ Назад</code> для отмены запроса.

    <b>Пишите на английском языке и обязательно ознакомьтесь с памяткой по созданию запросов → <a href="https://telegra.ph/Pamyatka-kak-sostavit-idealnyj-zapros-12-26">тык</a></b>

messages-tencentmaker  = 🤖 <i>Выбранная нейросеть:</i> <code>{ $neuro }</code>

    <b>Отправьте фотографию c подробным описанием того, что Вы хотите видеть на фотографии</b> или нажмите кнопку <code>⬅️ Назад</code> для отмены запроса.

    ⚠️ <i>Фотография без подписи обработана не будет!</i>

messages-enchance_image = 🤖 <i>Выбранная нейросеть:</i> <code>{ $neuro }</code>

    <b>Отправьте фотографию, которую нужно улучшить</b> или нажмите кнопку <code>⬅️ Назад</code> для отмены запроса.

messages-sdv_video = 🤖 <i>Выбранная нейросеть:</i> <code>{ $neuro }</code>

    <b>Отправьте фотографию, которую нужно анимировать</b> или нажмите кнопку <code>⬅️ Назад</code> для отмены запроса.

messages-whisper_voice = 🤖 <i>Выбранная нейросеть:</i> <code>{ $neuro }</code>

    <b>Отправьте аудиофайл, который нужно перевести в текст</b> или нажмите кнопку <code>⬅️ Назад</code> для отмены запроса.

messages-bender_voice = 🤖 <i>Выбранная нейросеть:</i> <code>{ $neuro }</code>

    <b>Введите текст, который нужно озвучить</b> или нажмите кнопку <code>⬅️ Назад</code> для отмены запроса.

```Requests```

messages-preps_for_photos = 🥰 <i>Готовлю ваши фотографии, пожалуйста, подождите...</i>

messages-request_processing = <b>Ваш запрос:</b> <code>{ $request }</code>

    😌 <i>Обработка запроса, пожалуйста, подождите...</i>

messages-request_result = <b>Ваш запрос:</b> <code>{ $request }</code>
    <i>Ответ нейросети:</i> { $result }

messages-image_processing = 🤖 <i>Выбранная нейросеть:</i> <code>{ $neuro }</code>

    <b>Ваш запрос:</b> <code>{ $prompt }</code>

    😌 <i>Обработка запроса, пожалуйста, подождите...</i>

messages-other_processing = 🤖 <i>Выбранная нейросеть:</i> <code>{ $neuro }</code>

    😌 <i>Обработка запроса, пожалуйста, подождите...</i>

messages-image_result = 🤖 _Выбранная нейросеть:_ `{ $neuro }`

    _Ваш запрос:_ `{ $prompt }`

messages-other_result = 🤖 <i>Выбранная нейросеть:</i> <code>{ $neuro }</code>

messages-answer = <i>Ответ нейросети:</i> <code>{ $result }</code>

```Chat mode```

messages-starting_chat = 🔄 Создаю новый диалог, пожалуйста, подождите...

messages-chat_mode = 🎉 <b>Диалог с ботом начат.</b> Для завершения диалога нажмите кнопку <code>{ $end_button }</code>.

messages-in_work = 😌 Один момент, пожалуйста, я обрабатываю ваш запрос...

messages-chat_answer = 🤖  

messages-stop_chatting = 👋 Диалог с ботом завершён, возвращаю Вас в главное меню.

```Admin panel```

messages-admin_panel = 👨‍💻 Панель администратора

messages-admin_find_user = 🔍 <b>Поиск пользователя</b>
    
    Введите NeuroID пользователя, которого хотите найти.

messages-admin_user_info = 👤 <b>Информация о пользователе</b>
    <i>Основная информация</i>

    👤 Имя >>> { $name }
    💬 NeuroID >>> <code>{ $neuro_id }</code>
    ⚙️ Количество совершённых генераций >>> <code>{ $request_counter }</code>

    📅 Дата регистрации >>> <code>{ $join_date }</code>

messages-admin_success_edit = ✅ Статус пользователя успешно изменен.

messages-admin_success = ✅ Статус нейросети успешно изменён.

messages-admin_success_maintenance = ✅ Статус технического обслуживания успешно изменён.

messages-admin_neuro_statuses = <b>🔥 Сменить статус нейросети</b>

    Нейросети для генерации текста:
    ├ ChatGPT: <code>{ $gpt }</code>
    ├ Claude AI: <code>{ $claude }</code>
    ├ Google AI: <code>{ $google }</code>
    ├ LLaMA AI: <code>{ $llama }</code>
    ├ Mistral AI (Medium): <code>{ $mistral }</code>
    ├ Solar AI: <code>{ $solar }</code>
    └ Google Gemini Pro: <code>{ $gemini }</code>

    Нейросети для генерации и обработки изображений:
    ├ StableDiffusionXL: <code>{ $stable }</code>
    ├ Playground v2: <code>{ $playground }</code>
    ├ EnhanceImage: <code>{ $enhance }</code>
    ├ Midjourney V4: <code>{ $midjourney }</code>
    ├ Midjourney V6: <code>{ $midjourneyv6 }</code>
    ├ StableDiffusion Video: <code>{ $sdv }</code>
    ├ DALL·E 3: <code>{ $dalle3 }</code>
    └ TencentARC PhotoMaker: <code>{ $tencentmaker }</code>

    Нейросети для работы с аудио:
    ├ Whisper V3: <code>{ $whisper }</code>
    └ RachelVoice: <code>{ $bender }</code>