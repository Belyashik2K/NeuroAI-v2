from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker 
from sqlalchemy import select, update, insert, text

from contextlib import asynccontextmanager

from config import Config
from notify import AdminNotify
from texts import OT

from .models import *

class Database:
    def __init__(self) -> None:
        """Initialize database."""
        self._engine = create_async_engine(
            url=Config.DB_PATH,
            echo=False
        )
        self._session = async_sessionmaker(
            self._engine, 
            expire_on_commit=False
            )
        self.__neuros = OT.neuro_names
        self.__notify = AdminNotify()
        
    @asynccontextmanager
    async def session(self) -> None:
        """Generate new session."""
        async with self._session() as session:
            try:
                yield session
            except:
                await session.rollback()
                raise
            finally:
                await session.close()
    
    async def create_tables(self) -> None:
        """Create tables in database."""
        async with self._engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        await self._engine.dispose()
        await self.prepare_tables()
        await self.add_user(Config.admin_id, 
                            full_name="Admin", 
                            username="Admin",
                            is_first_time=True)
        await self.update_user(Config.admin_id, is_admin=True)

    async def prepare_tables(self) -> None:
        """Add neuro statuses and settings to database."""
        async with self.session() as session:
            for neuro in self.__neuros:
                stmt = select(Neuros).where(Neuros.code_name == neuro)
                result = await session.execute(stmt)
                if not result.scalar_one_or_none():
                    stmt = insert(Neuros).values(code_name=neuro, is_active=False)
                    await session.execute(stmt)
                    await session.commit()
            stmt = select(Settings)
            result = await session.execute(stmt)
            if not result.scalar_one_or_none():
                stmt = insert(Settings).values(is_maintenance=False)
                await session.execute(stmt)
                await session.commit()

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
                       full_name: str = None, 
                       username: str = None,
                       is_first_time: bool = False
                       ) -> User:
        """Add user to database."""
        if not await self.get_user(user_id):
            async with self.session() as session:
                stmt = insert(User).values(
                    user_id=user_id,
                    full_name=full_name,
                    username=username
                )
                await session.execute(stmt)
                await session.commit()
                user = await self.get_user(user_id)
                if not is_first_time:
                    await self.__notify.new_user_notify(user.id, user.user_id, user.full_name)
        return await self.get_user(user_id)

    async def update_user(self, user_id: int, **kwargs) -> None:
        """Update user's info."""
        async with self.session() as session:
            stmt = update(User).where(User.user_id == user_id).values(**kwargs)
            await session.execute(stmt)
            await session.commit()

    async def get_stats(self) -> tuple[int, int, int, int, int]:
        """Get stats from database."""
        from datetime import datetime
        date = datetime.now().date()
        async with self.session() as session:
            stmt = text("SELECT COUNT(*) FROM users")
            result = await session.execute(stmt)
            users_count = result.fetchone()[0] or 0
            stmt = text("SELECT SUM(request_counter) FROM users")
            result = await session.execute(stmt)
            requests_count = result.fetchone()[0] or 0
        return [date.day if date.day > 10 else '0{}'.format(date.day),
                date.month if date.month > 10 else '0{}'.format(date.month), 
                date.year, 
                users_count, requests_count]
    
    async def get_neuro_statuses(self) -> dict[str, str]:
        """Get neuro statuses from database."""
        async with self.session() as session:
            from texts import UT
            stmt = select(Neuros)
            result = await session.execute(stmt)
            neuros = {}
            for neuro in result.fetchall():
                status = UT.AboutUs.working if neuro[0].is_active else UT.AboutUs.not_working
                neuros[neuro[0].code_name] = status
            neuros['support'] = Config.technical_support
            neuros['ads'] = Config.ads
            return neuros
                
    async def get_neuro(self, code_name: str) -> Neuros:
        """Get neuro from database."""
        async with self.session() as session:
            stmt = select(Neuros).where(Neuros.code_name == code_name)
            result = await session.execute(stmt)
            return result.scalar_one_or_none()
        
    async def get_users_count(self) -> int:
        """Get users count from database."""
        async with self.session() as session:
            stmt = text("SELECT COUNT(*) FROM users")
            result = await session.execute(stmt)
            return result.fetchone()[0] or 0
        
    async def get_users_list(self) -> list[int]:
        """Get user_id's from database."""
        async with self.session() as session:
            stmt = select(User.user_id)
            result = await session.execute(stmt)
            return [user[0] for user in result.fetchall()]
        
    async def get_admins(self) -> list[int]:
        """Get admin id's from database."""
        async with self.session() as session:
            stmt = select(User.user_id).where(User.is_admin == True)
            result = await session.execute(stmt)
            return [user[0] for user in result.fetchall()]
        
    async def switch_neuro_status(self, neuro_name: str) -> None:
        """Switch neuro status in database."""
        async with self.session() as session:
            stmt = select(Neuros).where(Neuros.code_name == neuro_name)
            result = await session.execute(stmt)
            neuro = result.scalar_one_or_none()
            stmt = update(Neuros).where(Neuros.code_name == neuro_name).values(is_active=not neuro.is_active)
            await session.execute(stmt)
            await session.commit()

    async def maintenance(self, is_for_update: bool = False) -> None:
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