

from controller.controller import Controller
from view.main_page_view import MainPageView

class MainPageController(Controller):
    def __init__(self):        
        self.main_page_view: MainPageView = MainPageView()
     
    def get_response(self) -> tuple[str, str]:        
        self.verify_query_string_parameters()        
        if self.response is not None:
            return self.response
        
        self.uuid = self.query_string_dict['uuid']
        
        self.get_match_info()        
        if self.response is not None:
            return self.response
            
        return ('200 OK', self.match_score_view.get_page(self.player_1_name, self.player_2_name, self.match.score), self.get_default_response_headers())
        
        