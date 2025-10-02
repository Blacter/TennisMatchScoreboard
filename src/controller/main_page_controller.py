from controller.controller import Controller
from view.main_page_view import MainPageView

class MainPageController(Controller):
    def __init__(self):        
        self.main_page_view: MainPageView = MainPageView()
        
    def get_response(self) -> tuple[str, str]: # @override ?
        return ('200 OK', self.main_page_view.get_page())
        
        