from abc import ABC, abstractmethod

from model.model import Model
from typealiases import ResponseHeaders
from view.view import View


class Controller(ABC):
    # def __init__(self, view: View, model: Model) -> None:
    #     self.view: View = view
    #     self.model: Model = model
        
    @abstractmethod
    def get_response(self) -> tuple[str, str]:
        pass
        
    def get_default_response_headers(self) -> ResponseHeaders:
        return [('Content-type', 'text/html')]
    
    