from contextlib import asynccontextmanager

from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from ..config import Config
from .models import *

class Database:
    def __init__(self):
        """Initialize database."""

        self._url = Config.DB.DB_URL

        self._engine = create_async_engine(
            url=self._url,
            echo=False
        )

        self._session = async_sessionmaker(
            self._engine, 
            expire_on_commit=False
            )
    
    @asynccontextmanager
    async def session(self):
        """Generate new session."""
        async with self._session() as session:
            try:
                yield session
            except:
                await session.rollback()
                raise
            finally:
                await session.close()
    
    async def create_tables(self):
        """Create tables in database."""
        async with self._engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        await self._engine.dispose()

    async def first_create(self) -> None:
        async with self.session() as session:
            stmt = select(Mailing)
            res = await session.execute(stmt)
            if not res.first():
                await session.execute(insert(Mailing).values(alive_users=0, died_users=0))
                await session.commit()
        
    async def get_mailing(self) -> Mailing:
        """Get mailing."""
        await self.first_create()
        async with self.session() as session:
            stmt = select(Mailing)
            res = await session.execute(stmt)
            return res.fetchone()[0]

    async def update(self, **kwargs):
        """Update mailing."""
        async with self.session() as session:
            await session.execute(update(Mailing).values(**kwargs))
            await session.commit()
            
    async def update_link_preview(self):
        """Update link preview."""
        async with self.session() as session:
            stmt = select(Mailing.link_preview)
            res = await session.execute(stmt)
            link_preview = not res.fetchall()[0][0]
            stmt = update(Mailing).values(link_preview=link_preview)
            await session.execute(stmt)
            await session.commit()
   
    async def get_stats(self):
        """Get mailing stats."""
        async with self.session() as session:
            stmt = select(Mailing.alive_users, Mailing.died_users)
            res = await session.execute(stmt)
            return res.fetchone()
    
    async def get_content_type(self):
        """Get mailing content type."""
        async with self.session() as session:
            stmt = select(Mailing.content_type)
            res = await session.execute(stmt)
            return res.fetchone()[0]
    
    async def reset_mailing(self):
        """Reset mailing stats."""
        stats = await self.get_stats()
        async with self.session() as session:
            await session.execute(delete(Mailing))
            await session.commit()
            await session.execute(insert(Mailing).values(alive_users=stats[0], died_users=stats[1]))
            await session.commit()