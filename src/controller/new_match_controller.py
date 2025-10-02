from controller.controller import Controller
from model.new_match_model import NewMatchModel
from view.new_match_view import NewMatchView


class NewMatchController(Controller):
    def __init__(self):
        self.new_match_view: NewMatchView = NewMatchView()
        self.new_match_model: NewMatchModel = NewMatchModel()
        
    def get_response(self) -> tuple[str, str]:
        return ('200 OK', self.new_match_view.get_page())
        