from .user import user_router
from .admin import admin_router
from .chat import chat_router

all_routers = [chat_router, admin_router, user_router]