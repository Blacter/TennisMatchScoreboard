from controller.controller import Controller
from controller.controller_exceptions.request_body_exception import RequestBodyException
from controller.response import Response
from model.new_match_create_model import NewMatchCreateModel
from model.model_exceptions.db_exceptions import DBException
from typealiases import ResponseHeaders
from view.new_match_create_view import NewMatchCreateView
from view.new_match_view import NewMatchView
from view.error_page_view import ErrorPageView

class NewMatchCreateController(Controller):
    def __init__(self, post_body: dict[str, str]):
        super().__init__()
        self.new_match_create_model: NewMatchCreateModel = NewMatchCreateModel()
        self.new_match_create_view: NewMatchCreateView = NewMatchCreateView()
        self.new_match_view: NewMatchView = NewMatchView()
        self.new_match_request_body: dict[str, str] = post_body
        self.error_description: str = ''
        
    def get_response(self) -> Response:
        try:
            self.verify_new_match_create_request_body()
        except RequestBodyException as e:
            return Response(code = '400 Bad Request',
                            body = self.new_match_view.get_page(is_error=True, error_description=str(e)),
                            headers = self.get_default_response_headers())        
        try:
            self.new_match_create_model.create_match(self.new_match_request_body)
        except DBException as e:
            error_page_view: ErrorPageView = ErrorPageView()
            return Response(code = '500 Internal Server Error',
                            body = error_page_view.get_page(str(e) + ' DBException'),
                            headers = self.get_default_response_headers())
        
        return Response(code = '302 Found',
                        body = self.new_match_create_view.get_page(),
                        headers = self.get_redirect_response_headers())

    def verify_new_match_create_request_body(self) -> None:
        self.check_request_body_keys()
        self.check_request_body_values()
    
    def get_redirect_response_headers(self) -> ResponseHeaders:
        return [('Location', '/match-score?uuid='+self.new_match_create_model.uuid)]
    
    def check_request_body_keys(self) -> None:
        if 'Player_1_name' not in self.new_match_request_body.keys():
            raise RequestBodyException('Key "Player_1_name" does not exist.')
        if 'Player_2_name' not in self.new_match_request_body.keys():
            raise RequestBodyException('Key "Player_2_name" does not exist.')
        
    def check_request_body_values(self) -> None:
        if self.is_empty_player_1_value():
            raise RequestBodyException('Player_1 should not be empty')
        if self.is_empty_player_2_value():
            raise RequestBodyException('Player_2 should not be empty')        
        
    def is_empty_player_1_value(self) -> bool:
        if len(self.new_match_request_body['Player_1_name']) == 0:
            return True
        return False
        
    def is_empty_player_2_value(self) -> bool:
        if len(self.new_match_request_body['Player_2_name']) == 0:
            return True
        return False