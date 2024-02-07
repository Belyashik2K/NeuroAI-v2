from datetime import datetime

from aiogram import html
from aiogram.utils.link import create_tg_link
from sqlalchemy import (BigInteger,
                        Integer,
                        String,
                        DateTime,
                        Boolean,
                        func)
from sqlalchemy.orm import Mapped, mapped_column as Column
from ...enums import Locale

from .base import Base


class User(Base):
    """User model.
    
    Attributes:
        id (int): User's id in database.
        user_id (int): User's id in Telegram.
        full_name (str): User's full name.
        username (str): User's username in Telegram.
        registered_at (datetime): User's registration date.
        last_activity (datetime): User's last activity.
        request_counter (int): User's request counter.
        locale (str): User's locale.
        first_language_set (bool): Is user's set his first language?
        is_admin (bool): Have user admin rights?
        is_banned (bool): Is user banned?
    """
    __tablename__ = 'users'

    id: Mapped[int] = Column(Integer, primary_key=True)
    user_id: Mapped[int] = Column(BigInteger(), unique=True, nullable=False)
    full_name: Mapped[str] = Column(String(255), nullable=False)
    username: Mapped[str] = Column(String(255))
    registered_at: Mapped[datetime] = Column(DateTime,
                                             server_default=func.now(),
                                             default=datetime.now,
                                             nullable=False)
    last_activity: Mapped[datetime] = Column(DateTime,
                                             server_default=func.now(),
                                             default=datetime.now,
                                             nullable=False)
    request_counter: Mapped[int] = Column(BigInteger(), default=0, nullable=False)
    locale: Mapped[str] = Column(String(2),
                                 server_default=Locale.DEFAULT,
                                 default=Locale.DEFAULT,
                                 nullable=False)
    first_language_set: Mapped[bool] = Column(Boolean,
                                              server_default="0",
                                              default=False,
                                              nullable=False)
    is_admin: Mapped[bool] = Column(Boolean, default=False, nullable=False)
    is_banned: Mapped[bool] = Column(Boolean, default=False, nullable=False)

    def __repr__(self) -> str:
        return f"<User(id={self.id}, user_id={self.user_id}, full_name={self.full_name}, username={self.username}, last_activity={self.last_activity}, locale={self.locale}, is_admin={self.is_admin})>"

    @property
    def url(self) -> str:
        """User's url in Telegram."""
        return create_tg_link("user", id=self.user_id)

    @property
    def mention(self) -> str:
        """User's mention in Telegram."""
        return html.link(value=self.full_name, link=self.url)
