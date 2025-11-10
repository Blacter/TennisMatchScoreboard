from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from model.base import Base

class Player(Base):
    __tablename__: str = 'players'    
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), index=True, unique=True)
