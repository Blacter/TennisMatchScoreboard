from abc import ABC, abstractmethod

from controller.response import Response
from model.model import Model
from typealiases import ResponseHeaders
from view.view import View


class Controller(ABC):
    def __init__(self):
        self.response: Response = None
        
    @abstractmethod
    def get_response(self) -> Response: # ? *args, **kwargs.
        pass
        
    def get_default_response_headers(self) -> ResponseHeaders:
        return [('Content-type', 'text/html')]
    
    