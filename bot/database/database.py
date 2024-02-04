import datetime

from typing import AsyncGenerator, Optional

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy import select, update, insert, func

from contextlib import asynccontextmanager

from aiogram_i18n import LazyProxy

from ..config import config
from ..enums import Locale, Category
from .models import User, Neuro, Settings, Chat
from ..keyboards.inline.callback import NeuroInfo

class Database:
    def __init__(self) -> None:
        """Initialize database."""
        url = config.sqlite_dsn if config.is_sqlite else config.postgres_dsn
        self._engine = create_async_engine(
            url=url,
            echo=False
        )
        self._session = async_sessionmaker(
            self._engine, 
            expire_on_commit=False
            )
    
    @asynccontextmanager
    async def session(self) -> AsyncGenerator[AsyncSession, None]:
        """Generate new session."""
        async with self._session() as session:
            try:
                yield session
            except:
                await session.rollback()
                raise
            finally:
                await session.close()
    
    async def prepare(self) -> None:
        """First preps for database"""
        async with self._engine.begin() as _:
            ...
        try:
            await self.add_user(user_id=config.admin_id,
                                full_name="Admin",
                                username="Admin",
                                locale=Locale.DEFAULT,
                                prepare=True,
                                first_launch=True)
            await self.prepare_tables()
        except:
            raise Exception("The current database tables haven't been updated. Perform the initial migration before starting work.")
        
    async def prepare_tables(self) -> None:
        """Add neuro statuses and settings to database."""
        async with self.session() as session:
            for provider, categories in NeuroInfo.neuros_alph.items():
                for category, names in categories.items():
                    for name in names:
                        stmt = select(Neuro).where(Neuro.code_name == name)
                        result = await session.execute(stmt)
                        if not result.scalar_one_or_none():
                            stmt = insert(Neuro).values(code_name=name,
                                                        provider=provider,
                                                        category=category,
                                                        is_active=name not in NeuroInfo.not_working)
                            await session.execute(stmt)
                            await session.commit()
            stmt = select(Settings)
            result = await session.execute(stmt)
            if not result.scalar_one_or_none():
                stmt = insert(Settings).values(is_maintenance=False)
                await session.execute(stmt)
                await session.commit()

    async def select_for_pagination(self,
                                    model: User,
                                    page: int,
                                    per_page: int,
                                    ) -> list[list[User], int]:
        """Select _ for pagination"""
        async with self.session() as session:
            stmt = select(model).offset((page - 1) * per_page).limit(per_page).order_by(model.id)
            result = await session.execute(stmt)
            data = result.scalars().all()
            
            stmt = select(func.count()).select_from(model)
            result = await session.execute(stmt)
            count = result.scalar_one_or_none()

            pages_count = count // per_page + 1 if (count % per_page and count) else count // per_page
            return data, pages_count

    async def get_user(self, 
                       user_id: int,
                       by_neuro_id: bool = False
                       ) -> User:
        """Get user from database."""
        async with self.session() as session:
            stmt = select(User).where(User.user_id == user_id if not by_neuro_id else User.id == user_id)
            result = await session.execute(stmt)
            return result.scalar_one_or_none()
        
    async def add_user(self, 
                       user_id: int, 
                       full_name: str, 
                       username: str,
                       locale: str,
                       prepare: Optional[bool] = False,
                       first_launch: Optional[bool] = False
                       ) -> User:
        """Add user to database."""
        locale = Locale.resolve(locale)
        if not await self.get_user(user_id):
            async with self.session() as session:
                stmt = insert(User).values(
                    user_id=user_id,
                    full_name=full_name,
                    username=username,
                    locale=locale,
                )
                await session.execute(stmt)
                await session.commit()
                if prepare:
                    await self.update_user(user_id, is_admin=True)
                if not first_launch:
                    user = await self.get_user(user_id)
                    from ..utils.notify import sender
                    await sender.new_user_notify(user.id, user.user_id, user.full_name)
        return await self.get_user(user_id)
    
    async def update_user(self, 
                          user_id: int, 
                          **kwargs
                          ) -> User:
        """Update user's info."""
        async with self.session() as session:
            stmt = update(User).where(User.user_id == user_id).values(**kwargs)
            await session.execute(stmt)
            await session.commit()
        return await self.get_user(user_id)

    async def update_last_activity(self, 
                                   user_id: int
                                   ) -> None:
        """Update user's last activity."""
        async with self.session() as session:
            stmt = update(User).where(User.user_id == user_id).values(last_activity=datetime.datetime.now())
            await session.execute(stmt)
            await session.commit()

    async def get_admins(self
                            ) -> list[int]:
        """Get admins' ids"""
        async with self.session() as session:
            stmt = select(User.user_id).where(User.is_admin)
            result = await session.execute(stmt)
            return result.scalars().all()
        
    async def get_users_count(self) -> int:
        """Get users' count"""
        async with self.session() as session:
            stmt = select(User.user_id)
            result = await session.execute(stmt)
            return len(result.fetchall())
        
    async def get_users_list(self) -> list[int]:
        """Get users' ids"""
        async with self.session() as session:
            stmt = select(User.user_id)
            result = await session.execute(stmt)
            return result.scalars().all()
        
    async def get_stats(self) -> tuple[int, int, int, int, int]:
        """Get stats from database."""
        from datetime import datetime
        async with self.session() as session:
            stmt = select(func.count(User.id)).select_from(User)
            result = await session.execute(stmt)
            users_count = result.scalar_one_or_none() or 0
            stmt = select(func.sum(User.request_counter)).select_from(User)
            result = await session.execute(stmt)
            requests_count = result.scalar_one_or_none() or 0
        
        date = datetime.now().date().strftime('%d.%m.%Y')

        return {"date": date,
                "users_count": users_count,
                "requests_count": requests_count}
    
    async def get_all_categories(self) -> list[str]:
        """Get all categories from database."""
        async with self.session() as session:
            stmt = select(Neuro.category).distinct()
            result = await session.execute(stmt)
            return result.scalars().all()
    
    async def get_neuros_by_category(self,
                                     category: str,
                                     page: int,
                                     per_page: int) -> list[list[Neuro], int]:
        """Get all neuros from database."""
        async with self.session() as session:
            stmt = select(Neuro).where(Neuro.category == category).offset((page - 1) * per_page).limit(per_page).order_by(Neuro.id)
            result = await session.execute(stmt)
            on_page = result.scalars().all()

            stmt = select(func.count()).select_from(Neuro).where(Neuro.category == category)
            result = await session.execute(stmt)
            count = result.scalar_one_or_none()

            pages_count = count // per_page + 1 if (count % per_page and count) else count // per_page

            return on_page, pages_count
    
    async def get_neuro_statuses(self) -> dict[str, str]:
        """Get neuro statuses from database."""
        async with self.session() as session:
            data = {}

            stmt = select(func.count()).select_from(Neuro)
            result = await session.execute(stmt)
            data['neuro_count'] = result.scalar_one_or_none()

            categories = [Category.TEXT, Category.IMAGE, Category.AUDIO]
            for category in categories:
                stmt = select(func.count()).select_from(Neuro).where(Neuro.category == category)
                result = await session.execute(stmt)
                neuro_count = result.scalar_one_or_none()

                stmt = select(func.count()).select_from(Neuro).where(Neuro.category == category).where(Neuro.is_active)
                result = await session.execute(stmt)
                neuro_active = result.scalar_one_or_none()

                data[f'{category}_working'] = neuro_active
                data[f'{category}_not_working'] = neuro_count - neuro_active

            data['support'] = config.technical_support
            data['ads'] = config.ads
            return data

    async def get_neuro(self, code_name: str) -> Neuro:
        """Get neuro from database."""
        async with self.session() as session:
            stmt = select(Neuro).where(Neuro.code_name == code_name)
            result = await session.execute(stmt)
            return result.scalar_one_or_none()
        
    async def switch_neuro_status(self, neuro_name: str) -> None:
        """Switch neuro status in database."""
        async with self.session() as session:
            neuro = await self.get_neuro(neuro_name)
            stmt = update(Neuro).where(Neuro.code_name == neuro_name).values(is_active=not neuro.is_active)
            await session.execute(stmt)
            await session.commit()

    async def maintenance(self, is_for_update: bool = False) -> bool:
        """Switch maintenance mode in database or get current status."""
        async with self.session() as session:
            stmt = select(Settings)
            result = await session.execute(stmt)
            settings = result.scalar_one_or_none()
            if is_for_update:
                stmt = update(Settings).values(is_maintenance=not settings.is_maintenance)
                await session.execute(stmt)
                await session.commit()
            return settings.is_maintenance

    async def get_chat(self, chat_id: int) -> Chat:
        """Get chat from database."""
        async with self.session() as session:
            stmt = select(Chat).where(Chat.chat_id == chat_id)
            result = await session.execute(stmt)
            return result.scalar_one_or_none()
        
    async def add_chat(self, chat_id: int) -> Chat:
        """Add chat to database."""
        if not await self.get_chat(chat_id):
            async with self.session() as session:
                stmt = insert(Chat).values(
                    chat_id=chat_id
                )
                await session.execute(stmt)
                await session.commit()
                chat = await self.get_chat(chat_id)
                await self.__notify.new_chat_notify(chat.chat_id, chat.id)
        return await self.get_chat(chat_id)
    
    async def update_chat(self, chat_id: int, **kwargs) -> None:
        """Update chat's info."""
        async with self.session() as session:
            stmt = update(Chat).where(Chat.chat_id == chat_id).values(**kwargs)
            await session.execute(stmt)
            await session.commit()
            