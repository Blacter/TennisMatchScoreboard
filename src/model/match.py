from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from model.base import Base


class Match(Base):
    __tablename__: str = 'matches'
    
    id: Mapped[Integer] = mapped_column(Integer, primary_key=True)
    uuid: Mapped[String] = mapped_column(String(20), unique=True)
    # ? Maybe use relationship ?
    player_1: Mapped[Integer] = mapped_column(Integer, ForeignKey('players.id'))
    player_2: Mapped[Integer] = mapped_column(Integer, ForeignKey('players.id'))
    winner: Mapped[Integer] = mapped_column(Integer, ForeignKey('players.id'), nullable=True)
    score: Mapped[String] = mapped_column(String(40))
    
    