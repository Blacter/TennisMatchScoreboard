import re
from sqlalchemy.exc import OperationalError
from sqlalchemy.exc import NoResultFound
# from pymysql.err import OperationalError
from typing import Sequence

from controller.controller import Controller
from controller.response import Response
from controller.controller_exceptions.query_string_exception import QueryStringException
from model.match import Match
from model.matches_model import MatchesModel
from model.model_exceptions.db_exceptions import DBException
from view.error_page_view import ErrorPageView
from view.matches_view import MatchesView


class MatchesController(Controller):
    def __init__(self, query_string_dict: dict[str, str]):
        super().__init__()
        self.matches_model: MatchesModel = MatchesModel()
        self.matches_view: MatchesView = MatchesView()
        self.error_page_view: ErrorPageView = ErrorPageView()
        self.query_raw: dict[str, str] = query_string_dict
        
    def get_response(self) -> Response:
        self.parse_query()
        if self.response is not None:
            return self.response
        
        self.get_matches()
        if self.response is not None:
            return self.response
        
        return Response(code = '200 OK',
                        body = self.matches_view.get_page(page_number=self.query['page'], filter_by_player_name=self.query['filter_by_player_name'], matches = self.matches), 
                        headers = self.get_default_response_headers())
        
    def parse_query(self) -> None:
        try:
            self._parse_query()
        except QueryStringException as e:
            self.response = Response(code = '400 Bad Request',
                                     body = self.error_page_view.get_page(str(e) + ' QueryStringException'),
                                     headers = self.get_default_response_headers())
            
    def get_matches(self) -> None:
        try:
            if self.query['filter_by_player_name'] == '':
                self.matches: Sequence[Match] = self.matches_model.get_matches_with_player_names(self.query['page'])
            else:
                self.matches: Sequence[Match] = self.matches_model.get_matches_with_player_names_with_filter(self.query['page'], self.query['filter_by_player_name'])
            print(f'{self.matches=}')
        except NoResultFound:
            self.response = Response(code = '200 OK',
                        body = self.matches_view.get_page(page_number=self.query['page'], filter_by_player_name=self.query['filter_by_player_name'], matches = None), 
                        headers = self.get_default_response_headers())
        except DBException as e:                
            self.response = Response(code = '500 Internal Server Error',
                                     body = self.error_page_view.get_page(str(e)),
                                     headers = self.get_default_response_headers())
        except OperationalError:
            self.response = Response(code = '500 Internal Server Error',
                                     body = self.error_page_view.get_page("Sorry, the service is temporary unavilable"),
                                     headers = self.get_default_response_headers())
    
    def _parse_query(self) -> None:
        self.query: dict[str, str] = {}
        self.parse_page()
        self.parse_filter_by_player_name()
            
    def parse_page(self) -> None:
        if 'page' in self.query_raw.keys():
            self.query['page'] = MatchesController.convert_to_int(self.query_raw['page'])
        else:
            self.query['page'] = 1
            
    def parse_filter_by_player_name(self) -> None:
        if 'filter_by_player_name' in self.query_raw.keys():
            self.query['filter_by_player_name'] = self.query_raw['filter_by_player_name']
        else:
            self.query['filter_by_player_name'] = ''
            
    @staticmethod
    def convert_to_int(num: str) -> int:
        if not MatchesController.is_int(num):
            raise QueryStringException('Can not convert page parametere to integer.')
        return int(num)
            
    @staticmethod    
    def is_int(num: str) -> bool:
        return re.match(r'^\d+$', num)
    