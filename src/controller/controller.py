from view import View
from model import Service

class Controller:
    def __init__(self, view: View, service: Service) -> None:
        self.view: View = view
        self.service: Service = service
        
    
    