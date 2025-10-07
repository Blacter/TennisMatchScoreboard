import re

from controller.controller import Controller
from controller.controller_exceptions.query_string_exception import QueryStringException
from model.player import Player
from model.match_score_model import MatchScoreModel
from model.match import Match
from model.model_exceptions.db_exceptions import DBException
from model.model_exceptions.uuid_exceptions import UuidException
from service.match_score_service import MatchScoreService
from view.match_score_view import MatchScoreView
from view.error_page_view import ErrorPageView

class MatchScoreController(Controller):
    def __init__(self, query_string_dict: dict[str, str]):
        self.match_score_model: MatchScoreModel = MatchScoreModel()        
        self.match_score_view: MatchScoreView = MatchScoreView()
        self.error_page_view: ErrorPageView = ErrorPageView()
        self.query_string_dict: dict[str, str] = query_string_dict
        self.response: tuple[str, str] | None = None
        
    def get_response(self) -> tuple[str, str]:        
        self.verify_query_string_parameters()        
        if self.response is not None:
            return self.response
        
        self.uuid = self.query_string_dict['uuid']
        
        self.get_match_info()        
        if self.response is not None:
            return self.response
            
        match_score_service: MatchScoreService = MatchScoreService(self.match.score)            
        return ('200 OK', self.match_score_view.get_page(self.player_1_name, self.player_2_name, match_score_service.to_dict()), self.get_default_response_headers())
    
    def verify_query_string_parameters(self) -> None:
        try:
            self._verify_query_string_parameters()
        except QueryStringException as e:            
            self.response = ('400 Bad Request', self.error_page_view.get_page(str(e) + ' QueryStringException'), self.get_default_response_headers())
            
    def get_match_info(self) -> None:
        try:            
            self._get_match_info()
        except UuidException as e:
            self.response = ('400 Bad Request', self.error_page_view.get_page(str(e)), self.get_default_response_headers())
        except DBException as e:
            self.response = ('500 Internal Server Error', self.error_page_view.get_page(str(e)), self.get_default_response_headers())
        
    def _verify_query_string_parameters(self) -> None:
        self.verify_uuid_key_exists()
        self.verify_uuid_value_format()
        
    def get_match_info(self) -> None:
        try:            
            self._get_match_info()
        except UuidException as e:
            self.response = ('400 Bad Request', self.error_page_view.get_page(str(e)), self.get_default_response_headers())
        except DBException as e:
            self.response = ('500 Internal Server Error', self.error_page_view.get_page(str(e)), self.get_default_response_headers())
        
    def _get_match_info(self) -> None:
        self.get_match()
        self.get_player_1_name()
        self.get_player_2_name()
        print(f'{self.match.score=}')
        print(f'{self.player_1_name=}')
        print(f'{self.player_2_name=}')
    
    def verify_uuid_key_exists(self) -> None:
        if 'uuid' not in self.query_string_dict.keys():
            raise QueryStringException('uuid key doesn\'t exists')
        
    def verify_uuid_value_format(self) -> None:
        uuid_pattern: str = r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'
        if not re.match(pattern=uuid_pattern, string=self.query_string_dict['uuid'], flags=re.IGNORECASE):
            raise QueryStringException('uuid wrong format')    
    
    def get_match(self) -> None:
        self.match: dict = self.match_score_model.get_match_by_uuid(self.uuid)
        
    def get_player_1_name(self) -> None:
        self.player_1_name: str = self.match_score_model.get_player_name_by_id(self.match.player_1)
        
        
    def get_player_2_name(self) -> None:
        self.player_2_name: str = self.match_score_model.get_player_name_by_id(self.match.player_2)        
