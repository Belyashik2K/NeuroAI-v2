class NotifyTexts:
    error = """😣 <b>An error occurred</b>

👤 User Information
├ ID >>> <code>{user_id}</code>
└ Mention >>> {mention}

📝 Error Information
└ Error >>> <code>{exception}</code>
"""

    new_user = """🎉 <b>New user in the bot!</b>

👤 User >>> <a href="tg://user?id={user_id}">{full_name}</a>
💬 NeuroID >>> <code>{neuro_id}</code>
"""

    new_chat = """🎉 <b>New chat in the bot!</b>

👥 Chat ID >>> <code>{chat_id}</code>
💬 NeuroID >>> <code>{neuro_id}</code>
"""
