from sqlalchemy.orm import sessionmaker
from sqlalchemy import select 
from sqlalchemy.exc import NoResultFound

from model.match import Match
from model.model import Model
from model.model_exceptions.db_exceptions import DBException
from model.model_exceptions.uuid_exceptions import UuidException
from model.player import Player


class MatchScoreModel(Model):
    def __init__(self):
        super().__init__()
        
    def get_match_by_uuid(self, uuid: str) -> Match:
        Session = sessionmaker(bind=self.engine)                
        with Session() as session:
            try: 
                statement = select(Match).where(Match.uuid == uuid)
                match: Match = session.scalars(statement).one()
                print(f'{match=}')
            except NoResultFound:
                raise UuidException()
            except DBException:                
                raise DBException()                
        return match
    
    def get_player_name_by_id(self, player_id: int) -> str:
        Session = sessionmaker(bind=self.engine)        
        with Session() as session:
            try:
                query = select(Player).where(Player.id == player_id)
                player: Player = session.scalars(query).one()
            except:
                raise DBException()            
        return player.name
    
    def update_match_score(self, match: Match) -> None:
        Session = sessionmaker(bind=self.engine)
        with Session() as session:
            try:
                session.merge(match)
            except:
                session.rollback()
                raise DBException()
            else:
                session.commit()
                