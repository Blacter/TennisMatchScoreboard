from abc import ABC, abstractmethod

from jinja2 import Environment, FileSystemLoader

from config import settings


type PageView = str

class View(ABC):
    def __init__(self):
        file_loader = FileSystemLoader(settings.TEMPLATES_PATH)
        self.env = Environment(loader=file_loader)
        
    
    @abstractmethod
    def get_page(self, **kwargs) -> PageView:
        pass
    