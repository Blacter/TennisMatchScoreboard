from controller.controller import Controller
from model.page_not_found_model import PageNotFoundModel
from view.page_not_found_view import PageNotFoundView



class PageNotFoundController(Controller):
    def __init__(self):
        self.page_not_found_model: PageNotFoundModel = PageNotFoundModel()
        self.page_not_found_view: PageNotFoundView = PageNotFoundView()
        
    def get_response(self) -> tuple[str, str]:
        return ('404 Not Found', self.page_not_found_view.get_page())
    