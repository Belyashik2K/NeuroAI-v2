import datetime

from sqlalchemy import (Integer,
                        DateTime,
                        BigInteger,
                        Boolean,
                        func)
from sqlalchemy.orm import Mapped, mapped_column as Column

from .base import Base

class Chat(Base):
    """Chat model.
    
    Attributes:
        id (int): Chat's id in database.
        chat_id (int): Chat's id in Telegram.
        registered_at (datetime): Chat's registration date.
        last_activity (datetime): Chat's last activity.
        request_counter (int): Chat's request counter.
        automatic_transcription (bool): Is automatic transcription enabled?
    """
    __tablename__ = 'chats'
    id: Mapped[int] = Column(Integer, primary_key=True)
    chat_id: Mapped[int] = Column(BigInteger, unique=True, nullable=False)
    registered_at: Mapped[DateTime] = Column(DateTime, 
                            server_default=func.now(),
                            default=datetime.datetime.now,
                            nullable=False)
    last_activity: Mapped[DateTime] = Column(DateTime, 
                            server_default=func.now(),
                            default=datetime.datetime.now, 
                            nullable=False)
    request_counter: Mapped[int] = Column(BigInteger, default=0, nullable=False)
    automatic_transcription: Mapped[bool] = Column(Boolean, default=True, nullable=False)

    def __repr__(self) -> str:
        return f'Chat(id={self.id}, chat_id={self.chat_id}, registered_at={self.registered_at}, last_activity={self.last_activity}, request_counter={self.request_counter})'