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
    — <b>Абсолютно бесплатен</b> и работаю на основе <a href="https://api.futureforge.dev/docs">API FutureForge</a> и <a href="https://visioncraft-rs24.koyeb.app/docs">API VisionCraft</a>
    — Имею <b>открытый</b> исходный код, который ты можешь найти в моем репозитории на <a href="https://github.com/Belyashik2K/NeuroAI-v2">GitHub</a>

    🆘 Техническая поддержка >>> { $technical_support }
    🥀 Сотрудничество >>> { $ads }

```Set language```

messages-choose_language = 🌐 <b>Сменить язык</b>

messages-lang_set = 🎉 Язык успешно изменен!

```Favourite neuros```

messages-favourite_neuro = 🌟 <b>Избранные нейросети</b>
    <i>Выберите одну из Ваших избранных нейросетей</i>

messages-no_favourite = 🌟 <b>Избранные нейросети</b>
    😕 <i>У Вас пока нет избранных нейросетей</i>

    <i>Чтобы добавить нейросеть в избранное, выберите её в меню <code>{ $select_neuro }</code> и нажмите кнопку</i> <code>{ $favourite_button }</code>

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

    🤖 Всего нейросетей: <code>{ $neuro_count }</code>
    🆘 Техническая поддержка: { $support }
    🥀 Cотрудничество: { $ads }

    🤔 <b>Статусы нейросетей</b>
    Нейросети для генерации текста:
    ├ Работает нейросетей: <code>{ $text_working }</code>
    └ На техническом обслуживании: <code>{ $text_not_working }</code>

    Нейросети для генерации и обработки изображений:
    ├ Работает нейросетей: <code>{ $image_working }</code>
    └ На техническом обслуживании: <code>{ $image_not_working }</code>

    Нейросети для работы с аудио:
    ├ Работает нейросетей: <code>{ $audio_working }</code>
    └ На техническом обслуживании: <code>{ $audio_not_working }</code>

messages-working = Работает

messages-not_working = На техническом обслуживании

```Neuro categories```

messages-choose_neuro_category = <b>🔥 Выбор нейросети</b>
    ❓ <i>Выберите категорию нейросети</i>
        
    📝 <code>Текст</code> — нейросети, которые генерируют текст.

    🖼 <code>Изображения</code> — нейросети, которые генерируют изображения.

    🎵 <code>Аудио</code> — нейросети, которые генерируют аудио.

```Neuro choose```

messages-choose_neuro = ❓ <b>Выберите нейросеть</b>

messages-category_text = <i>Выберите одну из представленных ниже нейросетей</i>

messages-category_image = <i>Выберите одну из представленных ниже нейросетей</i>

messages-category_audio = <i>Выберите одну из представленных ниже нейросетей</i>

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
    <i>Ответ нейросети: </i>

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
    ├ Работает нейросетей: <code>{ $text_working }</code>
    └ На техническом обслуживании: <code>{ $text_not_working }</code>

    Нейросети для генерации и обработки изображений:
    ├ Работает нейросетей: <code>{ $image_working }</code>
    └ На техническом обслуживании: <code>{ $image_not_working }</code>

    Нейросети для работы с аудио:
    ├ Работает нейросетей: <code>{ $audio_working }</code>
    └ На техническом обслуживании: <code>{ $audio_not_working }</code>

```Input field placeholders```

messages-main_menu = Выберите действие в меню ниже или напишите команду /start...