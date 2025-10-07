from controller.controller import Controller
from model.matches_model import MatchesModel
from view.matches_view import MatchesView

class MatchesController(Controller):
    def __init__(self):
        self.matches_model: MatchesModel = MatchesModel()
        self.matches_view: MatchesView = MatchesView()
        
    def get_response(self) -> tuple[str, str]:
        return ('200 OK', self.matches_view.get_page(), self.get_default_response_headers())
    