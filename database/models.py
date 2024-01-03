import datetime

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import (
                        Column, 
                        Integer, 
                        String, 
                        DateTime, 
                        Boolean,  
                        BigInteger
                        )

class Base(DeclarativeBase):
    pass

class User(Base):
    """User model.
    
    Attributes:
        id (int): User's id in database.
        user_id (int): User's id in Telegram.
        full_name (str): User's full name.
        username (str): User's username in Telegram.
        last_activity (datetime): User's last activity.
        request_counter (int): User's request counter.
        is_admin (bool): Have user admin rights?
        is_banned (bool): Is user banned?
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger, unique=True, nullable=False)
    full_name = Column(String(255), nullable=False)
    username = Column(String(255))
    registered_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    last_activity = Column(DateTime, default=datetime.datetime.now, nullable=False)
    request_counter = Column(BigInteger, default=0, nullable=False)
    is_admin = Column(Boolean, default=False, nullable=False)
    is_banned = Column(Boolean, default=False, nullable=False)

    def __repr__(self) -> str:
        return f'User(id={self.id}, user_id={self.user_id}, full_name={self.full_name}, username={self.username}, registered_at={self.registered_at}, last_activity={self.last_activity}, request_counter={self.request_counter}, is_admin={self.is_admin}, is_banned={self.is_banned})'

class Neuros(Base):
    """Neuro model.
    
    Attributes:
        id (int): Neuro's id in database.
        code_name (str): Neuro's code name.
        is_active (bool): Is neuro active?
    """
    __tablename__ = 'neuros'
    id = Column(Integer, primary_key=True)
    code_name = Column(String(255), nullable=False, unique=True)
    is_active = Column(Boolean, default=False, nullable=False)

    def __repr__(self) -> str:
        return f'Neuro(id={self.id}, code_name={self.code_name}, is_active={self.is_active})'
    
class Settings(Base):
    """Settings model.
    
    Attributes:
        is_maintenance (bool): Is bot in maintenance mode?
    """
    __tablename__ = 'settings'
    id = Column(Integer, primary_key=True)
    is_maintenance = Column(Boolean, default=False, nullable=False)

    def __repr__(self) -> str:
        return f'Settings(id={self.id}, is_maintenance={self.is_maintenance})'