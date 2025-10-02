from time import time

from sqlalchemy import select
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker

from model.match import Match
from model.model import Model
from model.player import Player


class NewMatchCreateModel(Model):
    def __init__(self):
        super().__init__()

    def create_match(self, new_match_request_body) -> None:
        self.create_player_if_not_exists(
            new_match_request_body['Player_1_name'])
        self.create_player_if_not_exists(
            new_match_request_body['Player_2_name'])

        self.select_player_1(new_match_request_body['Player_1_name'])
        self.select_player_2(new_match_request_body['Player_2_name'])

        self.add_match_in_database()

    def create_player_if_not_exists(self, player_name: str) -> None:
        if not self.is_player_exist(player_name):
            self.create_player(player_name)

    def select_player_1(self, player_name: str) -> None:
        Session = sessionmaker(bind=self.engine)
        with Session() as session:
            try: 
                statement = select(Player).where(Player.name == player_name)
            except:                
                raise
            else:               
                player = session.scalars(statement).one()
                self.player_1: Player = player

    def select_player_2(self, player_name: str) -> None:
        Session = sessionmaker(bind=self.engine)
        with Session() as session:
            try:
                statement = select(Player).where(Player.name == player_name)
            except:
                raise
            else:
                player = session.scalars(statement).one()
                self.player_2: Player = player
            
    def add_match_in_database(self):
        Session = sessionmaker(bind=self.engine)
        with Session() as session:
            try:
                match_to_add: Match = Match(uuid=str(time()), player_1=self.player_1.id, player_2=self.player_2.id, score='0:0')
                session.add(match_to_add)
            except:
                session.rollback()
                raise
            else:
                session.commit()

    def is_player_exist(self, player_name: str) -> bool:
        is_exist: bool = False
        with self.engine.connect() as conn:
            statement = select(Player).with_only_columns(
                func.count(Player.name)).where(Player.name == player_name)
            count_players_with_this_name = conn.scalars(statement).one()
            print(f'{count_players_with_this_name=}')
            if count_players_with_this_name == 1:
                is_exist = True
        return is_exist

    def create_player(self, player_name: str) -> None:
        Session = sessionmaker(bind=self.engine)
        with Session() as session:
            try:
                player_to_add: Player = Player(name=player_name)
                session.add(player_to_add)
            except:
                session.rollback()
                raise
            else:
                session.commit()
                self.player: Player = player_to_add
