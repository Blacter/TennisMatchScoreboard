from controller.controller import Controller
from controller.response import Response
from model.page_not_found_model import PageNotFoundModel
from view.page_not_found_view import PageNotFoundView



class PageNotFoundController(Controller):
    def __init__(self):
        super().__init__()
        self.page_not_found_model: PageNotFoundModel = PageNotFoundModel()
        self.page_not_found_view: PageNotFoundView = PageNotFoundView()
        
    def get_response(self) -> Response:
        return Response(code = '404 Not Found',
                        body = self.page_not_found_view.get_page(),
                        headers = self.get_default_response_headers())
    