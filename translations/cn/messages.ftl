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
    — <b>绝对免费</b>，基于 <a href="https://api.futureforge.dev/docs">API FutureForge</a> 和 <a href="https://visioncraft-rs24.koyeb.app/docs">API VisionCraft</a> 运行
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
    用于文本生成的神经网络：
    ├ 工作中的神经网络：<code>{ $text_working }</code>
    └ 技术维护中的神经网络：<code>{ $text_not_working }</code>

    用于图像生成和处理的神经网络：
    ├ 工作中的神经网络：<code>{ $image_working }</code>
    └ 技术维护中的神经网络：<code>{ $image_not_working }</code>

    用于音频处理的神经网络：
    ├ 工作中的神经网络：<code>{ $audio_working }</code>
    └ 技术维护中的神经网络：<code>{ $audio_not_working }</code>

messages-working = 工作中

messages-not_working = 正在技术维护

```Neuro categories```

messages-choose_neuro_category = <b>🔥 选择神经网络</b>
    ❓ <i>选择神经网络类别</i>
        
    📝 <code>文本</code> — 生成文本的神经网络。

    🖼 <code>图像</code> — 生成图像的神经网络。

    🎵 <code>音频</code> — 生成音频的神经网络。

```Neuro choose```

messages-choose_neuro = ❓ <b>选择神经网络</b>

messages-category_text = <i>请选择以下列出的其中一个神经网络</i>

messages-category_image = <i>请选择以下列出的其中一个神经网络</i>

messages-category_audio = <i>请选择以下列出的其中一个神经网络</i>

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
    <i>神经网络回答: </i>

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

messages-chat_answer = 🤖 

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
    ├ 工作中的神经网络：<code>{ $text_working }</code>
    └ 技术维护中的神经网络：<code>{ $text_not_working }</code>

    用于图像生成和处理的神经网络：
    ├ 工作中的神经网络：<code>{ $image_working }</code>
    └ 技术维护中的神经网络：<code>{ $image_not_working }</code>

    用于音频处理的神经网络：
    ├ 工作中的神经网络：<code>{ $audio_working }</code>
    └ 技术维护中的神经网络：<code>{ $audio_not_working }</code>

```Input field placeholders```

messages-main_menu = 在下面的菜单中选择操作或键入命令 /start...