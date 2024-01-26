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
    — <b>Абсолютно безкоштовний</b> і працюю на основі <a href="https://api.futureforge.dev/docs">API FutureForge</a>
    — Маю <b>відкритий</b> вихідний код, який ти можеш знайти в моєму репозиторії на <a href="https://github.com/Belyashik2K/NeuroAI-v2">GitHub</a>

    🆘 Технічна підтримка >>> { $technical_support }
    🥀 Співпраця >>> { $ads }

```Set language```

messages-choose_language = 🌐 <b>Змінити мову</b>

messages-lang_set = 🎉 Мову успішно змінено!

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
    ├ ChatGPT: <code>{ $gpt }</code>
    ├ Claude AI: <code>{ $claude }</code>
    ├ Google AI: <code>{ $google }</code>
    ├ LLaMA AI: <code>{ $llama }</code>
    ├ Mistral AI (Medium): <code>{ $mistral }</code>
    ├ Solar AI: <code>{ $solar }</code>
    └ Google Gemini Pro: <code>{ $gemini }</code>

    Нейромережі для генерації та обробки зображень:
    ├ StableDiffusionXL: <code>{ $stable }</code>
    ├ Playground v2: <code>{ $playground }</code>
    ├ EnhanceImage: <code>{ $enhance }</code>
    ├ Midjourney V4: <code>{ $midjourney }</code>
    ├ Midjourney V6: <code>{ $midjourneyv6 }</code>
    ├ StableDiffusion Video: <code>{ $sdv }</code>
    ├ DALL·E 3: <code>{ $dalle3 }</code>
    └ TencentARC PhotoMaker: <code>{ $tencentmaker }</code>
    
    Нейромережі для роботи з аудіо:
    ├ Whisper V3: <code>{ $whisper }</code>
    └ RachelVoice: <code>{ $bender }</code>

messages-working = Працює

messages-not_working = На технічному обслуговуванні

```Neuro categories```

messages-choose_neuro_category = <b>🔥 Вибір нейромережі</b>
    ❓ <i>Оберіть категорію нейромережі</i>
        
    📝 <code>Текст</code> — нейромережі, які генерують текст.
    <i>Список нейромереж:</i>
    ├ <code>💭 ChatGPT (GPT 3.5)</code>
    ├ <code>☁️ Claude AI</code>
    ├ <code>📱 Google AI</code>
    ├ <code>🦙 LLaMA AI</code>
    ├ <code>💻 Mistral AI (Medium)</code>
    ├ <code>🌤 Solar AI</code>
    └ <code>📚 Google Gemini Pro</code>

    🖼 <code>Зображення</code> — нейромережі, які генерують зображення.
    <i>Список нейромереж:</i>
    ├ <code>🎨 StableDiffusionXL</code>
    ├ <code>🎮 Playground v2</code>
    ├ <code>📷 Midjourney V4</code>
    ├ <code>🔥 Midjourney V6</code>
    ├ <code>✨ EnhanceImage</code>
    ├ <code>📹 StableDiffusion Video</code>
    ├ <code>🖼 DALL·E 3</code>
    └ <code>🖌 TencentARC PhotoMaker</code>

    🎵 <code>Аудіо</code> — нейромережі, які генерують аудіо.
    <i>Список нейромереж:</i>
    ├ <code>🎤 Whisper V3</code>
    └ <code>🗣️ RachelVoice</code>

```Neuro choose```

messages-choose_neuro = ❓ <b>Оберіть нейромережу</b>

messages-category_text = <code>💭 ChatGPT (GPT 3.5)</code> — одна з найстабільніших нейромереж для генерації тексту. Вона може генерувати текст, писати код, відповідати на питання та багато іншого. Може обробляти посилання на сайти.

    <code>☁️ Claude AI</code> —  асистент ШІ нового покоління, заснований на дослідженнях Anthropic з навчання корисним, чесним і безпечним системам ШІ. Claude здатний виконувати широкий спектр завдань з обробки розмов та тексту, зберігаючи при цьому високий рівень надійності і передбачуваності. Працює переважно з англійською мовою.

    <code>📱 Google AI</code> — нейромереж від Google, яка може генерувати тексти, переважно англійською мовою.

    <code>🦙 LLaMA AI</code> — велика мовна модель (LLM), випущена Meta AI в лютому 2023 року. Були навчені моделі різних розмірів в діапазоні від 7 до 65 мільярдів ваг.

    <code>💻 Mistral AI (Medium)</code> — велика мовна модель машинного навчання з семи мільярдами параметрів. Відповіді на рівні ChatGPT, але з більш високою якістю. Працює переважно з англійською мовою.

    <code>🌤 Solar AI</code> - модель від компанії Upstage займає провідні позиції в рейтингу HuggingFace Open LLM і є покращеною версією моделі LLaMA 2.

    <code>📚 Google Gemini Pro</code> — одна з найбільш передових нейромереж, випущена компанією Google. Вона може генерувати текст, дивитися на зображення і відповідати на питання як англійською, так і російською мовою.

messages-category_image = <code>🎨 StableDiffusionXL</code> — нейромереж, яка може генерувати зображення за вказаним запитом. Надає чіткі і якісні зображення при використанні хорошого промпта.

    <code>🎮 Playground v2</code> — одна з кращих нейромереж для генерації зображень. Здатна генерувати зображення за вказаним запитом.

    <code>📷 Midjourney V4</code> — нейромереж, яка може генерувати зображення за вказаним запитом. Надає чіткі і якісні зображення при використанні хорошого промпта.

    <code>🔥 Midjourney V6</code> — найкраща нейромережа для генерації зображень на даний момент. Покращена версія <code>📷 Midjourney V4</code>

    <code>✨ EnhanceImage</code> — нейромереж, яка може покращувати якість зображень.

    <code>📹 StableDiffusion Video</code> — нейромереж, яка може генерувати відео за отриманою фотографією.

    <code>🖼 DALL·E 3</code> — одна з найбільш передових нейромереж для генерації зображень від компанії OpenAI.

    <code>🖌 TencentARC PhotoMaker</code> — нейромережа, яка може створити будь-яке зображення з будь-яким обличчям за заданим запитом. Фільтр NSFW відсутній.

messages-category_audio = <code>🎤 Whisper V3</code> — нейромереж, яка може переводити аудіофайл в текст.

    <code>🗣 RachelVoice</code> — нейромереж, яка може генерувати аудіофайли за вказаним текстом.

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
    <i>Відповідь нейромережі:</i> { $result }

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

messages-chat_answer = 🤖 { $answer }

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
    ├ ChatGPT: <code>{ $gpt }</code>
    ├ Claude AI: <code>{ $claude }</code>
    ├ Google AI: <code>{ $google }</code>
    ├ LLaMA AI: <code>{ $llama }</code>
    ├ Mistral AI (Medium): <code>{ $mistral }</code>
    ├ Solar AI: <code>{ $solar }</code>
    └ Google Gemini Pro: <code>{ $gemini }</code>

    Нейромережі для генерації та обробки зображень:
    ├ StableDiffusionXL: <code>{ $stable }</code>
    ├ Playground v2: <code>{ $playground }</code>
    ├ EnhanceImage: <code>{ $enhance }</code>
    ├ Midjourney V4: <code>{ $midjourney }</code>
    ├ Midjourney V6: <code>{ $midjourneyv6 }</code>
    ├ StableDiffusion Video: <code>{ $sdv }</code>
    ├ DALL·E 3: <code>{ $dalle3 }</code>
    └ TencentARC PhotoMaker: <code>{ $tencentmaker }</code>

    Нейромережі для роботи з аудіо:
    ├ Whisper V3: <code>{ $whisper }</code>
    └ RachelVoice: <code>{ $bender }</code>