from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import (
                        Column, 
                        Integer, 
                        Boolean,  
                        Text, 
                        )

class Base(DeclarativeBase):
    pass

class Mailing(Base):
    __tablename__ = "mailing"

    id = Column(Integer, primary_key=True)
    text = Column(Text, default="Не установлен")
    button_text = Column(Text, default="Не установлен")
    button_link = Column(Text, default="Не установлена")
    media = Column(Text, default="Не установлено")
    link_preview = Column(Boolean, default=1)
    alive_users = Column(Integer, default=0)
    died_users = Column(Integer, default=0)
    content_type = Column(Text, default="text")