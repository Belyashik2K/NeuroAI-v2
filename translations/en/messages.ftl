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
    — <b>Absolutely free</b> and operates on the <a href="https://api.futureforge.dev/docs">FutureForge API</a>
    — I have <b>open-source</b> code that you can find in my repository on <a href="https://github.com/Belyashik2K/NeuroAI-v2">GitHub</a>

    🆘 Technical Support >>> { $technical_support }
    🥀 Collaboration >>> { $ads }

```Set language```

messages-choose_language = 🌐 <b>Change language</b>

messages-lang_set = 🎉 Language successfully changed!

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
    Text generation neural networks:
    ├ ChatGPT: <code>{ $gpt }</code>
    ├ Claude AI: <code>{ $claude }</code>
    ├ Google AI: <code>{ $google }</code>
    ├ LLaMA AI: <code>{ $llama }</code>
    ├ Mistral AI (Medium): <code>{ $mistral }</code>
    ├ Solar AI: <code>{ $solar }</code>
    └ Google Gemini Pro: <code>{ $gemini }</code>

    Image generation and processing neural networks:
    ├ StableDiffusionXL: <code>{ $stable }</code>
    ├ Playground v2: <code>{ $playground }</code>
    ├ EnhanceImage: <code>{ $enhance }</code>
    ├ Midjourney V4: <code>{ $midjourney }</code>
    ├ Midjourney V6: <code>{ $midjourneyv6 }</code>
    ├ StableDiffusion Video: <code>{ $sdv }</code>
    ├ DALL·E 3: <code>{ $dalle3 }</code>
    └ TencentARC PhotoMaker: <code>{ $tencentmaker }</code>

    Audio-related neural networks:
    ├ Whisper V3: <code>{ $whisper }</code>
    └ RachelVoice: <code>{ $bender }</code>

messages-working = Working

messages-not_working = Under technical maintenance

```Neuro categories```

messages-choose_neuro_category = <b>🔥 Choose Neural Network</b>
    ❓ <i>Choose the neural network category</i>
        
    📝 <code>Text</code> — networks that generate text.
    <i>List of networks:</i>
    ├ <code>💭 ChatGPT (GPT 3.5)</code>
    ├ <code>☁️ Claude AI</code>
    ├ <code>📱 Google AI</code>
    ├ <code>🦙 LLaMA AI</code>
    ├ <code>💻 Mistral AI (Medium)</code>
    ├ <code>🌤 Solar AI</code>
    └ <code>📚 Google Gemini Pro</code>

    🖼 <code>Images</code> — networks that generate images.
    <i>List of networks:</i>
    ├ <code>🎨 StableDiffusionXL</code>
    ├ <code>🎮 Playground v2</code>
    ├ <code>📷 Midjourney V4</code>
    ├ <code>🔥 Midjourney V6</code>
    ├ <code>✨ EnhanceImage</code>
    ├ <code>📹 StableDiffusion Video</code>
    ├ <code>🖼 DALL·E 3</code>
    └ <code>🖌 TencentARC PhotoMaker</code>

    🎵 <code>Audio</code> — networks that generate audio.
    <i>List of networks:</i>
    ├ <code>🎤 Whisper V3</code>
    └ <code>🗣️ RachelVoice</code>

```Neuro choose```

messages-choose_neuro = ❓ <b>Choose the neural network</b>

messages-category_text = <code>💭 ChatGPT (GPT 3.5)</code> — one of the most stable text generation networks. It can generate texts, write code, answer questions, and more. Can process links to websites.

    <code>☁️ Claude AI</code> — next-generation AI assistant based on Anthropic's research on training useful, honest, and harmless AI systems. Claude can perform a wide range of tasks in conversation and text processing, maintaining high reliability and predictability. Primarily works with the English language.

    <code>📱 Google AI</code> — Google's neural network capable of generating texts, primarily in English.

    <code>🦙 LLaMA AI</code> — a large language model (LLM) released by Meta AI in February 2023. Models of various sizes were trained ranging from 7 to 65 billion parameters.

    <code>💻 Mistral AI (Medium)</code> — a large language model with seven billion parameters. Answers at the level of ChatGPT but with higher quality. Primarily works with the English language.

    <code>🌤 Solar AI</code> - a model from Upstage that holds leading positions in the HuggingFace Open LLM ranking and is an improved version of the LLaMA 2 model.

    <code>📚 Google Gemini Pro</code> — one of the most advanced neural networks released by Google. It can generate texts, analyze images, and answer questions in both English and Russian.

messages-category_image = <code>🎨 StableDiffusionXL</code> — a network capable of generating images based on a given prompt. Provides clear and high-quality images with a good prompt.

    <code>🎮 Playground v2</code> — one of the best networks for image generation. Capable of generating images based on a given prompt.

    <code>📷 Midjourney V4</code> — a network capable of generating images based on a given prompt. Provides clear and high-quality images with a good prompt.

    <code>🔥 Midjourney V6</code> — best neural network for image generation currently. Improved version of <code>📷 Midjourney V4</code>
    
    <code>✨ EnhanceImage</code> — a network capable of enhancing the quality of images.

    <code>📹 StableDiffusion Video</code> — a network capable of generating videos based on a received photo.

    <code>🖼 DALL·E 3</code> — one of the most advanced networks for image generation from OpenAI.

    <code>🖌 TencentARC PhotoMaker</code> — A neural network capable of generating any image with any face based on the given request. NSFW filter is not present.

messages-category_audio = <code>🎤 Whisper V3</code> — a network capable of translating audio files into text.

    <code>🗣 RachelVoice</code> — a network capable of generating audio files based on a given text.

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
    <i>Neural network response:</i> { $result }

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

messages-chat_answer = 🤖 { $answer }

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

    Text generation neural networks:
    ├ ChatGPT: <code>{ $gpt }</code>
    ├ Claude AI: <code>{ $claude }</code>
    ├ Google AI: <code>{ $google }</code>
    ├ LLaMA AI: <code>{ $llama }</code>
    ├ Mistral AI (Medium): <code>{ $mistral }</code>
    ├ Solar AI: <code>{ $solar }</code>
    └ Google Gemini Pro: <code>{ $gemini }</code>

    Image generation and processing neural networks:
    ├ StableDiffusionXL: <code>{ $stable }</code>
    ├ Playground v2: <code>{ $playground }</code>
    ├ EnhanceImage: <code>{ $enhance }</code>
    ├ Midjourney V4: <code>{ $midjourney }</code>
    ├ Midjourney V6: <code>{ $midjourneyv6 }</code>
    ├ StableDiffusion Video: <code>{ $sdv }</code>
    ├ DALL·E 3: <code>{ $dalle3 }</code>
    └ TencentARC PhotoMaker: <code>{ $tencentmaker }</code>

    Audio-related neural networks:
    ├ Whisper V3: <code>{ $whisper }</code>
    └ RachelVoice: <code>{ $bender }</code>