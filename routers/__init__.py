from .user import user_router
from .admin import admin_router

all_routers = [admin_router, user_router]