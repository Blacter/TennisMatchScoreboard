from controller.controller import Controller
from controller.response import Response
from view.main_page_view import MainPageView


class MainPageController(Controller):
    def __init__(self):        
        super().__init__()
        self.main_page_view: MainPageView = MainPageView()
     
    def get_response(self) -> Response:
        return Response(code = '200 OK',
                        body = self.main_page_view.get_page(),
                        headers = self.get_default_response_headers())
        
        