```Start```

messages-start = 🙋 Hello, { $name }!
    
    <b>To continue working with the bot, please choose one of the languages below 👇</b>

    ⚠️ <i>After choosing the language, you can change it in the</i> <code>👤 My Account</code>

messages-info = 🙋 Welcome to the world of neural networks, { $name }!
    
    I am { $self }, an updated version of the NeuroAI bot that will help you work with neural networks conveniently and effectively!

    <b>My advantages:</b>
    — I answer your questions in a <b>dialogue</b> or <b>single-message</b> format
    — I generate <b>photos</b> based on a given request
    — I generate audio files based on a given request and translate them
    — <b>Absolutely free</b> and operates based on <a href="https://api.futureforge.dev/docs">API FutureForge</a> and <a href="https://api.visioncraft.top/docs">API VisionCraft</a>
    — I have <b>open-source</b> code that you can find in my repository on <a href="https://github.com/Belyashik2K/NeuroAI-v2">GitHub</a>

    🆘 Technical Support >>> { $technical_support }
    🥀 Collaboration >>> { $ads }

```Set language```

messages-choose_language = 🌐 <b>Change language</b>

messages-lang_set = 🎉 Language successfully changed!

```Favourite neuros```

messages-favourite_neuro = 🌟 <b>Favorite neural networks</b>
    <i>Choose one of your favorite neural networks</i>

messages-no_favourite = 🌟 <b>Favorite neural networks</b>
    😕 <i>You currently have no favorite neural networks</i>

    <i>To add a neural network to favorites, select it in the menu <code>{ $select_neuro }</code> and press the button</i> <code>{ $favourite_button }</code>

```Profile info```

messages-my_profile = 👤 <b>My Account</b>
    <i>Main Information</i>

    👤 Name >>> { $name }
    💬 NeuroID >>> <code>{ $neuro_id }</code>
    ⚙️ Number of generations performed >>> <code>{ $request_counter }</code>

    📅 Registration Date >>> <code>{ $join_date }</code>

```Stats```

messages-stats = ✨ <b>Statistics</b>
    <i>On { $date }</i>

    👤 Users: <code>{ $users_count }</code>
    🔎 Generations by bot users: <code>{ $requests_count }</code>

```About + Neuro statuses```

messages-about = 💬 <b>About the service</b>
    <i>Main information and links</i>

    🆘 Technical Support: { $support }
    🥀 Collaboration: { $ads }

    🤔 <b>Neural Network Statuses</b>
    Neural networks for text generation:
    ├ Working neural networks: <code>{ $text_working }</code>
    └ Under technical maintenance: <code>{ $text_not_working }</code>

    Neural networks for image generation and processing:
    ├ Working neural networks: <code>{ $image_working }</code>
    └ Under technical maintenance: <code>{ $image_not_working }</code>

    Neural networks for audio processing:
    ├ Working neural networks: <code>{ $audio_working }</code>
    └ Under technical maintenance: <code>{ $audio_not_working }</code>

messages-working = Working

messages-not_working = Under technical maintenance

```Neuro categories```

messages-choose_neuro_category = <b>🔥 Choose Neural Network</b>
    ❓ <i>Choose the neural network category</i>
        
    📝 <code>Text</code> — networks that generate text.

    🖼 <code>Images</code> — networks that generate images.

    🎵 <code>Audio</code> — networks that generate audio.

```Neuro choose```

messages-choose_neuro = ❓ <b>Choose the neural network</b>

messages-category_text = <i>Choose one of the neural networks listed below</i>

messages-category_image = <i>Choose one of the neural networks listed below</i>

messages-category_audio = <i>Choose one of the neural networks listed below</i>

messages-mode = 🤖 <i>Selected network:</i> <code>{ $neuro }</code>

    ❓ <b>Choose the operating mode</b>
        
    🔥 <code>Single Request</code> — the bot will generate one response to your request and send it to you.

    👥 <code>Chat-bot</code> — the bot will respond to your messages until you end the dialogue.

messages-header = 🤖 <i>Selected network:</i> <code>{ $neuro }</code>
    <i>❓ Selected mode:</i> <code>{ $mode }</code>

messages-one_request_mode = <b>Enter your request</b> or press the <code>⬅️ Back</code> button to cancel the request.

messages-start_gen_image = 🤖 <i>Selected network:</i> <code>{ $neuro }</code>
        
    <b>Enter your request</b> or press the <code>⬅️ Back</code> button to cancel the request.

    <b>Write in English and be sure to check the guide on creating requests → <a href="https://telegra.ph/Pamyatka-kak-sostavit-idealnyj-zapros-12-26">here</a></b>

messages-tencentmaker = 🤖 <i>Selected neural network:</i> <code>{ $neuro }</code>

    <b>Send a photo with a detailed description of what you want to see in the photo</b> or press the <code>⬅️ Back</code> button to cancel the request.

    ⚠️ <i>A photo without a caption will not be processed!</i>

messages-enchance_image = 🤖 <i>Selected network:</i> <code>{ $neuro }</code>

    <b>Send the photo you want to enhance</b> or press the <code>⬅️ Back</code> button to cancel the request.

messages-sdv_video = 🤖 <i>Selected network:</i> <code>{ $neuro }</code>

    <b>Send the photo you want to animate</b> or press the <code>⬅️ Back</code> button to cancel the request.

messages-whisper_voice = 🤖 <i>Selected network:</i> <code>{ $neuro }</code>

    <b>Send the audio file you want to translate into text</b> or press the <code>⬅️ Back</code> button to cancel the request.

messages-bender_voice = 🤖 <i>Selected network:</i> <code>{ $neuro }</code>

    <b>Enter the text you want to voice</b> or press the <code>⬅️ Back</code> button to cancel the request.

```Requests```

messages-request_processing = <b>Your request:</b> <code>{ $request }</code>

    😌 <i>Processing your request, please wait...</i>

messages-request_result = <b>Your request:</b> <code>{ $request }</code>
    <i>Neural network response: </i>

messages-image_processing = 🤖 <i>Selected network:</i> <code>{ $neuro }</code>

    <b>Your request:</b> <code>{ $prompt }</code>

    😌 <i>Processing your request, please wait...</i>

messages-other_processing = 🤖 <i>Selected network:</i> <code>{ $neuro }</code>

    😌 <i>Processing your request, please wait...</i>

messages-image_result = 🤖 _Selected network:_ `{ $neuro }`

    _Your request:_ `{ $prompt }`

messages-other_result = 🤖 <i>Selected network:</i> <code>{ $neuro }</code>

messages-answer = <i>Neural network response:</i> <code>{ $result }</code>

```Chat mode```

messages-starting_chat = 🔄 Creating a new dialogue, please wait...

messages-chat_mode = 🎉 <b>Dialogue with the bot started.</b> To end the dialogue, press the <code>{ $end_button }</code> button.

messages-in_work = 😌 One moment, please. I am processing your request...

messages-chat_answer = 🤖 

messages-stop_chatting = 👋 The dialogue with the bot has ended, returning you to the main menu.

```Admin panel```

messages-admin_panel = 👨‍💻 Administrator Panel

messages-admin_find_user = 🔍 <b>Search for a user</b>
    
    Enter the NeuroID of the user you want to find.

messages-admin_user_info = 👤 <b>User Information</b>
    <i>Main Information</i>

    👤 Name >>> { $name }
    💬 NeuroID >>> <code>{ $neuro_id }</code>
    ⚙️ Number of generations performed >>> <code>{ $request_counter }</code>

    📅 Registration Date >>> <code>{ $join_date }</code>

messages-admin_success_edit = ✅ User status successfully changed.

messages-admin_success = ✅ Neural network status successfully changed.

messages-admin_success_maintenance = ✅ Technical maintenance status successfully changed.

messages-admin_neuro_statuses = <b>🔥 Change neural network status</b>

    Neural networks for text generation:
    ├ Working neural networks: <code>{ $text_working }</code>
    └ Under technical maintenance: <code>{ $text_not_working }</code>

    Neural networks for image generation and processing:
    ├ Working neural networks: <code>{ $image_working }</code>
    └ Under technical maintenance: <code>{ $image_not_working }</code>

    Neural networks for audio processing:
    ├ Working neural networks: <code>{ $audio_working }</code>
    └ Under technical maintenance: <code>{ $audio_not_working }</code>

```Input field placeholders```

messages-main_menu = Choose an action in the menu below or type the command /start...