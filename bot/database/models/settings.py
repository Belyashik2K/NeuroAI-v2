from sqlalchemy import (Integer,
                        Boolean)
from sqlalchemy.orm import Mapped, mapped_column as Column

from .base import Base


class Settings(Base):
    """Settings model.
    
    Attributes:
        id (int): Settings's id in database.
        is_maintenance (bool): Is bot in maintenance mode?
    """
    __tablename__ = 'settings'
    id: Mapped[int] = Column(Integer, primary_key=True)
    is_maintenance: Mapped[bool] = Column(Boolean, default=False, nullable=False)

    def __repr__(self) -> str:
        return f'Settings(id={self.id}, is_maintenance={self.is_maintenance})'
