from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from typing import Sequence

from config import settings
from model.model import Model
from model.match import Match
from model.player import Player
from model.model_exceptions.db_exceptions import DBException


class MatchesModel(Model):
    def __init__(self):
        super().__init__()
        
    def get_matches_with_player_names(self, page_number: int) -> Sequence[Match]:
        self.page_number = page_number
        self.get_matches()
        self.replace_player_ids_with_player_names()
        return self.matches_with_player_names
    
    def get_matches_with_player_names_with_filter(self, page_number: int, player_name: str) -> Sequence[Match]:
        self.page_number = page_number
        self.player_name = player_name
        self.get_matches_with_player_name()
        self.replace_player_ids_with_player_names()
        return self.matches_with_player_names
        
    def get_matches(self) -> list[Match]:
        step: int = int(settings.MATCHES_PER_PAGE)
        start_id: int = 1 + step*(self.page_number - 1)
        finish_id: int = start_id + step
        Session = sessionmaker(bind=self.engine)
        with Session() as session:
            try:
                query = session.query(Match).filter((Match.id >= start_id) & (Match.id < finish_id))
                self.matches_with_player_ids: Sequence[Match] = session.scalars(query).all()
                matches_to_print: list[str] = []
                for match in self.matches_with_player_ids:
                    matches_to_print.append(str(match))
                # for match_to_print in matches_to_print:
                #     print(f'{match_to_print=}')
            except NoResultFound:
                raise NoResultFound()
            except DBException:                
                raise DBException()
            
    def get_matches_with_player_name(self) -> list[Match]:
        step: int = int(settings.MATCHES_PER_PAGE)
        start_number: int = 1 + step*(self.page_number - 1)
        finish_number: int = start_number + step
        Session = sessionmaker(bind=self.engine)
        with Session() as session:
            try:
                player_id: int = session.query(Player).filter(Player.name == self.player_name).one().id
                query = select(Match).filter((Match.player_1 == player_id) | (Match.player_2 == player_id))
                self.matches_with_player_ids: Sequence[Match] = session.scalars(query).all()[start_number-1: finish_number-1]
                matches_to_print: list[str] = []
                for match in self.matches_with_player_ids:
                    matches_to_print.append(str(match))
            except NoResultFound:
                raise NoResultFound()
            except DBException:                
                raise DBException()

    def replace_player_ids_with_player_names(self) -> None:
        self.matches_with_player_names: list = []
        self.player_id_name_cache: dict[int, str] = {}
        for match_with_player_ids in self.matches_with_player_ids:
            match_with_player_name: dict = self.get_match_with_player_name_dict(match_with_player_ids)
            self.matches_with_player_names.append(match_with_player_name)
        
            
    def get_match_with_player_name_dict(self, match_with_player_ids) -> dict:
        match_tmp: dict = match_with_player_ids.to_dict()
        match_tmp['player_1'] = self.get_player_name_by_id(match_with_player_ids.player_1)
        match_tmp['player_2'] = self.get_player_name_by_id(match_with_player_ids.player_2)
        if match_tmp['winner'] is not None:
            match_tmp['winner'] = self.get_player_name_by_id(match_with_player_ids.winner)
        else:
            match_tmp['winner'] = '-'
        return match_tmp
    
    def get_player_name_by_id(self, player_id: int) -> str:
        if player_id not in self.player_id_name_cache.keys():
            self.player_id_name_cache[player_id] = self.get_player_name_by_id_from_db(player_id)        
        return self.player_id_name_cache[player_id]
    
    def get_player_name_by_id_from_db(self, player_id: int) -> str:
        Session = sessionmaker(bind=self.engine)
        with Session() as session:
            try:
                query = select(Player).where(Player.id == player_id)
                player: Player = session.scalars(query).one()
            except NoResultFound:
                raise NoResultFound()
            except DBException:                
                raise DBException()
        return player.name
    