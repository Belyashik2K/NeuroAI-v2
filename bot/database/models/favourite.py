from sqlalchemy import (Integer,
                        String,
                        BigInteger)
from sqlalchemy.orm import Mapped, mapped_column as Column

from .base import Base

class Favourite(Base):
    """Model for favourite neuros.
    
    Attributes:
        id (int): Favourite neuro's id in database.
        user_id (int): User's id
        neuro_name (str): Neuro's name.
    """
    __tablename__ = 'favourites'
    id: Mapped[int] = Column(Integer, primary_key=True)
    user_id: Mapped[int] = Column(BigInteger, nullable=False)
    neuro_name: Mapped[str] = Column(String(255), nullable=False)
    
    def __repr__(self) -> str:
        return f'Favourite(id={self.id}, user_id={self.user_id}, neuro_name={self.neuro_name})'
    