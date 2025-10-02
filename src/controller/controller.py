from abc import ABC, abstractmethod


from model.model import Model
from view.view import View


class Controller(ABC):
    # def __init__(self, view: View, model: Model) -> None:
    #     self.view: View = view
    #     self.model: Model = model
        
    @abstractmethod
    def get_response(self) -> tuple[str, str]:
        pass
        
    
    