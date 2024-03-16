```Start```

messages-start = 🙋 Привіт, { $name }!
    
    <b>Для продовження роботи з ботом, будь ласка, обери одну з мов нижче 👇</b>

    ⚠️ <i>Після обрання мови, ти зможеш змінити її в розділі</i> <code>👤 Мій обліковий запис</code>

messages-info = 🙋 Ласкаво просимо в світ нейромереж, { $name }!
    
    Я — { $self }, оновлена версія бота NeuroAI, яка допоможе тобі зручно і ефективно працювати з нейромережами!

    <b>Мої переваги:</b>
    — Відповідаю на твої питання у форматі <b>діалогу</b> або <b>одиночного повідомлення</b>
    — Генерую <b>фотографії</b> за вказаним запитом
    — Генерую аудіофайли за вказаним запитом і перекладаю їх
    — <b>Абсолютно безкоштовно</b> та працюю на основі <a href="https://api.futureforge.dev/docs">API FutureForge</a> та <a href="https://api.visioncraft.top/docs">API VisionCraft</a>
    — Маю <b>відкритий</b> вихідний код, який ти можеш знайти в моєму репозиторії на <a href="https://github.com/Belyashik2K/NeuroAI-v2">GitHub</a>

    🆘 Технічна підтримка >>> { $technical_support }
    🥀 Співпраця >>> { $ads }

```Set language```

messages-choose_language = 🌐 <b>Змінити мову</b>

messages-lang_set = 🎉 Мову успішно змінено!

```Favourite neuros```

messages-favourite_neuro = 🌟 <b>Обрані нейромережі</b>
    <i>Виберіть одну з ваших обраних нейромереж</i>

messages-no_favourite = 🌟 <b>Обрані нейромережі</b>
    😕 <i>Наразі у вас немає обраних нейромереж</i>

    <i>Щоб додати нейромережу до обраних, виберіть її у меню <code>{ $select_neuro }</code> і натисніть кнопку</i> <code>{ $favourite_button }</code>


```Profile info```

messages-my_profile = 👤 <b>Мій обліковий запис</b>
    <i>Основна інформація</i>

    👤 Ім'я >>> { $name }
    💬 NeuroID >>> <code>{ $neuro_id }</code>
    ⚙️ Кількість здійснених генерацій >>> <code>{ $request_counter }</code>

    📅 Дата реєстрації >>> <code>{ $join_date }</code>

```Stats```

messages-stats = ✨ <b>Статистика</b>
    <i>На { $date }</i>

    👤 Користувачів: <code>{ $users_count }</code>
    🔎 Генерацій користувачами бота: <code>{ $requests_count }</code>

```About + Neuro statuses```

messages-about = 💬 <b>Про сервіс</b>
    <i>Основна інформація та посилання</i>

    🆘 Технічна підтримка: { $support }
    🥀 Співпраця: { $ads }

    🤔 <b>Статуси нейромереж</b>
    Нейромережі для генерації тексту:
    ├ Працюють нейромережі: <code>{ $text_working }</code>
    └ На технічному обслуговуванні: <code>{ $text_not_working }</code>

    Нейромережі для генерації та обробки зображень:
    ├ Працюють нейромережі: <code>{ $image_working }</code>
    └ На технічному обслуговуванні: <code>{ $image_not_working }</code>

    Нейромережі для роботи з аудіо:
    ├ Працюють нейромережі: <code>{ $audio_working }</code>
    └ На технічному обслуговуванні: <code>{ $audio_not_working }</code>

messages-working = Працює

messages-not_working = На технічному обслуговуванні

```Neuro categories```

messages-choose_neuro_category = <b>🔥 Вибір нейромережі</b>
    ❓ <i>Оберіть категорію нейромережі</i>
        
    📝 <code>Текст</code> — нейромережі, які генерують текст.

    🖼 <code>Зображення</code> — нейромережі, які генерують зображення.

    🎵 <code>Аудіо</code> — нейромережі, які генерують аудіо.

```Neuro choose```

messages-choose_neuro = ❓ <b>Оберіть нейромережу</b>

messages-category_text = <i>Звільніть одну з представлених нижче нейромереж</i>

messages-category_image = <i>Звільніть одну з представлених нижче нейромереж</i>

messages-category_audio = <i>Звільніть одну з представлених нижче нейромереж</i>

messages-mode = 🤖 <i>Обрана нейромережа:</i> <code>{ $neuro }</code>
        
    ❓ <b>Оберіть режим роботи</b>
        
    🔥 <code>Одиночний запит</code> — бот згенерує одну відповідь на ваш запит і відправить вам її.

    👥 <code>Чат-бот</code> — бот буде відповідати на ваші повідомлення, поки ви не завершите діалог.

messages-header = 🤖 <i>Обрана нейромережа:</i> <code>{ $neuro }</code>
    <i>❓ Обраний режим:</i> <code>{ $mode }</code>

messages-one_request_mode = <b>Введіть ваш запит</b> або натисніть кнопку <code>⬅️ Назад</code> для скасування запиту.

messages-start_gen_image = 🤖 <i>Обрана нейромережа:</i> <code>{ $neuro }</code>
        
    <b>Введіть ваш запит</b> або натисніть кнопку <code>⬅️ Назад</code> для скасування запиту.

    <b>Пишіть англійською мовою та обов'язково ознайомтеся з пам'яткою по створенню запитів → <a href="https://telegra.ph/Pamyatka-kak-sostavit-idealnyj-zapros-12-26">тут</a></b>

messages-tencentmaker = 🤖 <i>Обрана нейромережа:</i> <code>{ $neuro }</code>

    <b>Відправте фотографію з докладним описом того, що ви хочете бачити на фотографії</b> або натисніть кнопку <code>⬅️ Назад</code> для скасування запиту.

    ⚠️ <i>Фотографія без підпису не буде оброблена!</i>

messages-enchance_image = 🤖 <i>Обрана нейромережа:</i> <code>{ $neuro }</code>

    <b>Надішліть фотографію, яку потрібно покращити</b> або натисніть кнопку <code>⬅️ Назад</code> для скасування запиту.

messages-sdv_video = 🤖 <i>Обрана нейромережа:</i> <code>{ $neuro }</code>

    <b>Надішліть фотографію, яку потрібно анімувати</b> або натисніть кнопку <code>⬅️ Назад</code> для скасування запиту.

messages-whisper_voice = 🤖 <i>Обрана нейромережа:</i> <code>{ $neuro }</code>

    <b>Надішліть аудіофайл, який потрібно перекласти в текст</b> або натисніть кнопку <code>⬅️ Назад</code> для скасування запиту.

messages-bender_voice = 🤖 <i>Обрана нейромережа:</i> <code>{ $neuro }</code>

    <b>Введіть текст, який потрібно озвучити</b> або натисніть кнопку <code>⬅️ Назад</code> для скасування запиту.

```Requests```

messages-request_processing = <b>Ваш запит:</b> <code>{ $request }</code>

    😌 <i>Обробка запиту, будь ласка, зачекайте...</i>

messages-request_result = <b>Ваш запит:</b> <code>{ $request }</code>
    <i>Відповідь нейромережі: </i>

messages-image_processing = 🤖 <i>Обрана нейромережа:</i> <code>{ $neuro }</code>

    <b>Ваш запит:</b> <code>{ $prompt }</code>

    😌 <i>Обробка запиту, будь ласка, зачекайте...</i>

messages-other_processing = 🤖 <i>Обрана нейромережа:</i> <code>{ $neuro }</code>

    😌 <i>Обробка запиту, будь ласка, зачекайте...</i>

messages-image_result = 🤖 _Обрана нейромережа:_ `{ $neuro }`

    _Ваш запит:_ `{ $prompt }`

messages-other_result = 🤖 <i>Обрана нейромережа:</i> <code>{ $neuro }</code>

messages-answer = <i>Відповідь нейромережі:</i> <code>{ $result }</code>

```Chat mode```

messages-starting_chat = 🔄 Створюю новий діалог, будь ласка, зачекайте...

messages-chat_mode = 🎉 <b>Діалог з ботом почато.</b> Для завершення діалогу натискайте кнопку <code>{ $end_button }</code>.

messages-in_work = 😌 Хвилинку, будь ласка, я обробляю ваш запит...

messages-chat_answer = 🤖 

messages-stop_chatting = 👋 Діалог з ботом завершено, повертаю Вас в головне меню.

```Admin panel```

messages-admin_panel = 👨‍💻 Панель адміністратора

messages-admin_find_user = 🔍 <b>Пошук користувача</b>
    
    Введіть NeuroID користувача, якого хочете знайти.

messages-admin_user_info = 👤 <b>Інформація про користувача</b>
    <i>Основна інформація</i>

    👤 Ім'я >>> { $name }
    💬 NeuroID >>> <code>{ $neuro_id }</code>
    ⚙️ Кількість виконаних генерацій >>> <code>{ $request_counter }</code>

    📅 Дата реєстрації >>> <code>{ $join_date }</code>

messages-admin_success_edit = ✅ Статус користувача успішно змінено.

messages-admin_success = ✅ Статус нейромережі успішно змінено.

messages-admin_success_maintenance = ✅ Статус технічного обслуговування успішно змінено.

messages-admin_neuro_statuses = <b>🔥 Змінити статус нейромережі</b>

    Нейромережі для генерації тексту:
    ├ Працюють нейромережі: <code>{ $text_working }</code>
    └ На технічному обслуговуванні: <code>{ $text_not_working }</code>

    Нейромережі для генерації та обробки зображень:
    ├ Працюють нейромережі: <code>{ $image_working }</code>
    └ На технічному обслуговуванні: <code>{ $image_not_working }</code>

    Нейромережі для роботи з аудіо:
    ├ Працюють нейромережі: <code>{ $audio_working }</code>
    └ На технічному обслуговуванні: <code>{ $audio_not_working }</code>

```Input field placeholders```

messages-main_menu = Виберіть дію в меню нижче або напишіть команду /start...