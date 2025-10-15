import uuid

from sqlalchemy import Integer, String, ForeignKey, BINARY
from sqlalchemy.orm import Mapped, mapped_column

from model.base import Base


class Match(Base):
    __tablename__: str = 'matches'
    
    id: Mapped[Integer] = mapped_column(Integer, primary_key=True)
    uuid: Mapped[String] = mapped_column(String(36), nullable=False, unique=True, default=uuid.uuid4)
    # ? Maybe use relationship ?
    player_1: Mapped[Integer] = mapped_column(Integer, ForeignKey('players.id'))
    player_2: Mapped[Integer] = mapped_column(Integer, ForeignKey('players.id'))
    winner: Mapped[Integer] = mapped_column(Integer, ForeignKey('players.id'), nullable=True)
    score: Mapped[String] = mapped_column(String(40))
    
    def __str__(self) -> str:
        return f'id: {self.id} | player_1: {self.player_1} | player_2: {self.player_2} | winner: {self.winner} | score: {self.score}'
    
    def to_dict(self) -> dict:
        match_dict: dict = {}
        match_dict['id'] = self.id
        match_dict['uuid'] = self.uuid
        match_dict['player_1'] = self.player_1
        match_dict['player_2'] = self.player_2
        match_dict['winner'] = self.winner
        match_dict['score'] = self.score
        
        return match_dict
    