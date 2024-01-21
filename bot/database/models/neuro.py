from sqlalchemy import (Integer,
                        String,
                        Boolean)
from sqlalchemy.orm import Mapped, mapped_column as Column

from .base import Base

class Neuro(Base):
    """Neuro model.
    
    Attributes:
        id (int): Neuro's id in database.
        code_name (str): Neuro's code name.
        is_active (bool): Is neuro active?
    """
    __tablename__ = 'neuros'
    
    id: Mapped[int] = Column(Integer, primary_key=True)
    code_name: Mapped[str] = Column(String(255), nullable=False, unique=True)
    is_active: Mapped[bool] = Column(Boolean, default=False, nullable=False)

    def __repr__(self) -> str:
        return f'Neuro(id={self.id}, code_name={self.code_name}, is_active={self.is_active})'
