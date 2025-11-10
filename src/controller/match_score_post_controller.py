from controller.controller_exceptions.request_body_exception import RequestBodyException
from controller.match_score_controller import MatchScoreController
from controller.response import Response
from model.model_exceptions.db_exceptions import DBException
from service.match_score_service import MatchScoreService


class MatchScorePostController(MatchScoreController):
    def __init__(self, query_string_dict: dict[str, str], post_body: dict[str, str] | None = None):
        super().__init__(query_string_dict)
        self.post_body: dict[str, str] = post_body
        
    def get_response(self) -> Response:        
        self.verify_query_string_parameters()        
        if self.response is not None:
            return self.response
        
        self.uuid = self.query_string_dict['uuid']
        
        self.verify_match_score_request_body()
        if self.response is not None:
            return self.response
        
        self.get_match_info()        
        if self.response is not None:
            return self.response
        
        self.change_match_state()
        if self.response is not None:
            return self.response
        
        match_score_service: MatchScoreService = MatchScoreService(self.match.score)
            
        return Response(code = '200 OK',
                        body = self.match_score_view.get_page(self.player_1_name, self.player_2_name, match_score_service.to_dict(), self.winner_name),
                        headers = self.get_default_response_headers())
        
    def verify_match_score_request_body(self) -> None:
        try:
            self.verify_keys()
        except RequestBodyException as e:    
            self.response = Response(code = '400 Bad Request',
                                     body = self.error_page_view.get_page(str(e)),
                                     headers = self.get_default_response_headers())                
        
    def change_match_state(self) -> None:
        self.renew_match_state_value()
        try:
            self.save_match_state_in_db()
        except DBException as e:
            self.response = Response(code = '500 Internal Server Error',
                                     body = self.error_page_view.get_page(str(e)), 
                                     headers = self.get_default_response_headers())
            
    def verify_keys(self) -> None:
        if not self.player_first_win_key_in_body_xor_player_two_win_key_in_body():
            raise RequestBodyException('The request body should contain one and only one key: "player_first_win" or "player_second_win"')
        
    def player_first_win_key_in_body_xor_player_two_win_key_in_body(self) -> bool:
        return 'player_first_win' in self.post_body.keys() and 'player_second_win' not in self.post_body.keys() \
                or 'player_first_win' not in self.post_body.keys() and 'player_second_win' in self.post_body.keys()
                
    def renew_match_state_value(self) -> None:
        self.match_score_service: MatchScoreService = MatchScoreService(self.match.score)
        self.renew_match_score_value()
        self.renew_match_winner_value()
        
    def renew_match_score_value(self) -> None:
        if self.is_player_one_win_one_score() and not self.was_winner():
            self.match_score_service.increase_player_one_score_on_one_point()            
        elif not self.was_winner():
            self.match_score_service.increase_player_two_score_on_one_point()
        self.match.score = self.match_score_service.get_match_score_in_str_format()

    def renew_match_winner_value(self) -> None:
        if self.match_score_service.player_one_win == True:
            self.match.winner = self.match.player_1
            self.get_winner_name()
        elif self.match_score_service.player_two_win == True:
            self.match.winner = self.match.player_2
            self.get_winner_name()
            print(f'{self.match.winner = }')
        
    def save_match_state_in_db(self) -> None:
        self.match_score_model.update_match_state(self.match)    
                
    def is_player_one_win_one_score(self) -> bool:
        return 'player_first_win' in self.post_body.keys()
