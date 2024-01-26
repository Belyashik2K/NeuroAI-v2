```Start```

messages-start = 🙋 你好，{ $name }！
    
    <b>要继续使用机器人，请选择下面的一种语言 👇</b>

    ⚠️ <i>选择语言后，你可以在</i> <code>👤 我的帐户</code> <i>部分更改它</i>

messages-info = 🙋 欢迎来到神经网络世界，{ $name }！
    
    我是 { $self }，是 NeuroAI 机器人的更新版本，将帮助你方便而高效地使用神经网络！

    <b>我的优势：</b>
    — 以<b>对话</b>或<b>单一消息</b>格式回答你的问题
    — 根据指定的请求生成<b>照片</b>
    — 根据指定的请求生成音频文件并翻译它们
    — <b>完全免费</b>，基于 <a href="https://api.futureforge.dev/docs">FutureForge API</a> 运行
    — 具有 <b>开放源代码</b>，你可以在我的 <a href="https://github.com/Belyashik2K/NeuroAI-v2">GitHub 仓库</a> 中找到

    🆘 技术支持 >>> { $technical_support }
    🥀 合作 >>> { $ads }

```Set language```

messages-choose_language = 🌐 <b>切换语言</b>

messages-lang_set = 🎉 语言已成功更改！

```Profile info```

messages-my_profile = 👤 <b>我的帐户</b>
    <i>基本信息</i>

    👤 名字 >>> { $name }
    💬 NeuroID >>> <code>{ $neuro_id }</code>
    ⚙️ 已生成数量 >>> <code>{ $request_counter }</code>

    📅 注册日期 >>> <code>{ $join_date }</code>

```Stats```

messages-stats = ✨ <b>统计</b>
    <i>{ $date } 的数据</i>

    👤 用户数: <code>{ $users_count }</code>
    🔎 机器人用户生成的请求数: <code>{ $requests_count }</code>

```About + Neuro statuses```

messages-about = 💬 <b>关于服务</b>
    <i>基本信息和链接</i>

    🆘 技术支持: { $support }
    🥀 合作: { $ads }

    🤔 <b>神经网络状态</b>
    用于文本生成的神经网络:
    ├ ChatGPT: <code>{ $gpt }</code>
    ├ Claude AI: <code>{ $claude }</code>
    ├ Google AI: <code>{ $google }</code>
    ├ LLaMA AI: <code>{ $llama }</code>
    ├ Mistral AI (Medium): <code>{ $mistral }</code>
    ├ Solar AI: <code>{ $solar }</code>
    └ Google Gemini Pro: <code>{ $gemini }</code>

    用于图像生成和处理的神经网络:
    ├ StableDiffusionXL: <code>{ $stable }</code>
    ├ Playground v2: <code>{ $playground }</code>
    ├ EnhanceImage: <code>{ $enhance }</code>
    ├ Midjourney V4: <code>{ $midjourney }</code>
    ├ Midjourney V6: <code>{ $midjourneyv6 }</code>
    ├ StableDiffusion Video: <code>{ $sdv }</code>
    ├ DALL·E 3: <code>{ $dalle3 }</code>
    └ TencentARC PhotoMaker: <code>{ $tencentmaker }</code>

    用于音频处理的神经网络:
    ├ Whisper V3: <code>{ $whisper }</code>
    └ RachelVoice: <code>{ $bender }</code>

messages-working = 工作中

messages-not_working = 正在技术维护

```Neuro categories```

messages-choose_neuro_category = <b>🔥 选择神经网络</b>
    ❓ <i>选择神经网络类别</i>
        
    📝 <code>文本</code> — 生成文本的神经网络。
    <i>神经网络列表：</i>
    ├ <code>💭 ChatGPT (GPT 3.5)</code>
    ├ <code>☁️ Claude AI</code>
    ├ <code>📱 Google AI</code>
    ├ <code>🦙 LLaMA AI</code>
    ├ <code>💻 Mistral AI (Medium)</code>
    ├ <code>🌤 Solar AI</code>
    └ <code>📚 Google Gemini Pro</code>

    🖼 <code>图像</code> — 生成图像的神经网络。
    <i>神经网络列表：</i>
    ├ <code>🎨 StableDiffusionXL</code>
    ├ <code>🎮 Playground v2</code>
    ├ <code>✨ EnhanceImage</code>
    ├ <code>📷 Midjourney V4</code>
    ├ <code>🔥 Midjourney V6</code>
    ├ <code>📹 StableDiffusion Video</code>
    ├ <code>🖼 DALL·E 3</code>
    └ <code>🖌 TencentARC PhotoMaker</code>

    🎵 <code>音频</code> — 生成音频的神经网络。
    <i>神经网络列表：</i>
    ├ <code>🎤 Whisper V3</code>
    └ <code>🗣️ RachelVoice</code>

```Neuro choose```

messages-choose_neuro = ❓ <b>选择神经网络</b>

messages-category_text = <code>💭 ChatGPT (GPT 3.5)</code> — 生成文本的稳定神经网络之一。能够生成文本、编写代码、回答问题等。可以处理网站链接。

    <code>☁️ Claude AI</code> — 下一代基于Anthropic研究的AI系统的助手。Claude能够处理各种对话和文本处理任务，并保持高可靠性和可预测性。主要使用英语。

    <code>📱 Google AI</code> — 谷歌推出的神经网络，主要能够生成英语文本。

    <code>🦙 LLaMA AI</code> — 由Meta AI于2023年2月发布的大型语言模型（LLM）。从7亿到65亿个参数的不同规模的模型都进行了训练。

    <code>💻 Mistral AI (Medium)</code> — 具有70亿参数的大型语言模型。在ChatGPT水平上回答，但质量更高。主要使用英语。

    <code>🌤 Solar AI</code> - 由Upstage公司推出的模型在HuggingFace Open LLM排行榜上名列前茅，是LLaMA 2模型的升级版。

    <code>📚 Google Gemini Pro</code> — 谷歌推出的最先进的神经网络之一。能够生成文本，查看图像并用英语和俄语回答问题。

messages-category_image = <code>🎨 StableDiffusionXL</code> — 能够根据请求生成清晰高质量图像的神经网络。

    <code>🎮 Playground v2</code> — 生成图像的最佳神经网络之一。能够根据请求生成图像。

    <code>📷 Midjourney V4</code> — 能够根据请求生成清晰高质量图像的神经网络。

    <code>🔥 Midjourney V6</code> — 目前最佳的图像生成神经网络。<code>📷 Midjourney V4</code> 的改进版本

    <code>✨ EnhanceImage</code> — 能够提高图像质量的神经网络。

    <code>📹 StableDiffusion Video</code> — 能够根据提供的照片生成视频的神经网络。

    <code>🖼 DALL·E 3</code> — 由OpenAI推出的最先进的图像生成神经网络之一。

    <code>🖌 腾讯ARC PhotoMaker</code> — 一种神经网络，能够根据给定的请求生成带有任何面孔的任何图像。不包含NSFW过滤器。

messages-category_audio = <code>🎤 Whisper V3</code> — 能够将音频文件转换为文本的神经网络。

    <code>🗣 RachelVoice</code> — 能够根据提供的文本生成音频文件的神经网络。

messages-mode = 🤖 <i>已选择神经网络：</i> <code>{ $neuro }</code>

    ❓ <b>选择工作模式</b>
        
    🔥 <code>单一请求</code> — 机器人将为您的请求生成一个回答并发送给您。

    👥 <code>聊天机器人</code> — 机器人将回复您的消息，直到您结束对话。

messages-header = 🤖 <i>已选择神经网络：</i> <code>{ $neuro }</code>
    <i>❓ 选择的工作模式：</i> <code>{ $mode }</code>

messages-one_request_mode = <b>输入您的请求</b> 或点击 <code>⬅️ 返回</code> 取消请求。

messages-start_gen_image = 🤖 <i>已选择神经网络：</i> <code>{ $neuro }</code>
        
    <b>输入您的请求</b> 或点击 <code>⬅️ 返回</code> 取消请求。

    <b>请使用英语书写，并务必阅读有关创建请求的提示 → <a href="https://telegra.ph/Pamyatka-kak-sostavit-idealnyj-zapros-12-26">这里</a></b>

messages-tencentmaker = 🤖 <i>选择的神经网络：</i> <code>{ $neuro }</code>

    <b>发送一张照片，并详细描述您想在照片中看到的内容</b> 或按下 <code>⬅️ 返回</code> 按钮取消请求。

    ⚠️ <i>没有标题的照片将不会被处理！</i>

messages-enchance_image = 🤖 <i>已选择神经网络：</i> <code>{ $neuro }</code>

    <b>发送您想要改进的照片</b> 或点击 <code>⬅️ 返回</code> 取消请求。

messages-sdv_video = 🤖 <i>已选择神经网络：</i> <code>{ $neuro }</code>

    <b>发送您想要制作动画的照片</b> 或点击 <code>⬅️ 返回</code> 取消请求。

messages-whisper_voice = 🤖 <i>已选择神经网络：</i> <code>{ $neuro }</code>

    <b>发送要转换为文本的音频文件</b> 或点击 <code>⬅️ 返回</code> 取消请求。

messages-bender_voice = 🤖 <i>已选择神经网络：</i> <code>{ $neuro }</code>

    <b>输入要转为语音的文本</b> 或点击 <code>⬅️ 返回</code> 取消请求。

```Requests```

messages-request_processing = <b>您的请求：</b> <code>{ $request }</code>

    😌 <i>处理请求中，请稍候...</i>

messages-request_result = <b>您的请求：</b> <code>{ $request }</code>
    <i>神经网络回答：</i> { $result }

messages-image_processing = 🤖 <i>已选择神经网络：</i> <code>{ $neuro }</code>

    <b>您的请求：</b> <code>{ $prompt }</code>

    😌 <i>处理请求中，请稍候...</i>

messages-other_processing = 🤖 <i>已选择神经网络：</i> <code>{ $neuro }</code>

    😌 <i>处理请求中，请稍候...</i>

messages-image_result = 🤖 _已选择神经网络:_ `{ $neuro }`

    _您的请求:_ `{ $prompt }`

messages-other_result = 🤖 <i>已选择神经网络：</i> <code>{ $neuro }</code>

messages-answer = <i>神经网络回答：</i> <code>{ $result }</code>

```Chat mode```

messages-starting_chat = 🔄 正在创建新的对话，请稍候...

messages-chat_mode = 🎉 <b>与机器人的对话已开始。</b> 要结束对话，请按下 <code>{ $end_button }</code> 按钮。

messages-in_work = 😌 请稍等，我正在处理您的请求...

messages-chat_answer = 🤖 { $answer }

messages-stop_chatting = 👋 与机器人的对话已结束，正在返回主菜单。

```Admin panel```

messages-admin_panel = 👨‍💻 管理员面板

messages-admin_find_user = 🔍 <b>查找用户</b>
    
    输入您要查找的用户的 NeuroID。

messages-admin_user_info = 👤 <b>用户信息</b>
    <i>主要信息</i>

    👤 姓名 >>> { $name }
    💬 NeuroID >>> <code>{ $neuro_id }</code>
    ⚙️ 已完成的请求次数 >>> <code>{ $request_counter }</code>

    📅 注册日期 >>> <code>{ $join_date }</code>

messages-admin_success_edit = ✅ 用户状态已成功更改。

messages-admin_success = ✅ 神经网络状态已成功更改。

messages-admin_success_maintenance = ✅ 技术维护状态已成功更改。

messages-admin_neuro_statuses = <b>🔥 更改神经网络状态</b>

    用于文本生成的神经网络：
    ├ ChatGPT: <code>{ $gpt }</code>
    ├ Claude AI: <code>{ $claude }</code>
    ├ Google AI: <code>{ $google }</code>
    ├ LLaMA AI: <code>{ $llama }</code>
    ├ Mistral AI (Medium): <code>{ $mistral }</code>
    ├ Solar AI: <code>{ $solar }</code>
    └ Google Gemini Pro: <code>{ $gemini }</code>

    用于图像生成和处理的神经网络：
    ├ StableDiffusionXL: <code>{ $stable }</code>
    ├ Playground v2: <code>{ $playground }</code>
    ├ EnhanceImage: <code>{ $enhance }</code>
    ├ Midjourney V4: <code>{ $midjourney }</code>
    ├ Midjourney V6: <code>{ $midjourneyv6 }</code>
    ├ StableDiffusion Video: <code>{ $sdv }</code>
    ├ DALL·E 3: <code>{ $dalle3 }</code>
    └ TencentARC PhotoMaker: <code>{ $tencentmaker }</code>

    用于音频处理的神经网络：
    ├ Whisper V3: <code>{ $whisper }</code>
    └ RachelVoice: <code>{ $bender }</code>