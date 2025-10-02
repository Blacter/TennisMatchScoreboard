from controller.controller import Controller
from model.match_score_model import MatchScoreModel
from view.match_score_view import MatchScoreView

class MatchScoreController(Controller):
    def __init__(self):
        self.match_score_model: MatchScoreModel = MatchScoreModel()
        self.match_score_view: MatchScoreView = MatchScoreView()
        
    def get_response(self) -> tuple[str, str]:
        return ('200 OK', self.match_score_view.get_page())
        