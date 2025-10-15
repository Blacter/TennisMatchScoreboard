from controller.controller import Controller
from controller.response import Response
from model.new_match_model import NewMatchModel
from view.new_match_view import NewMatchView


class NewMatchController(Controller):
    def __init__(self):
        super().__init__()
        self.new_match_view: NewMatchView = NewMatchView()
        self.new_match_model: NewMatchModel = NewMatchModel()

    def get_response(self) -> Response:
        return Response(code = '200 OK',
                        body = self.new_match_view.get_page(),
                        headers = self.get_default_response_headers())
        