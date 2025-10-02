import os

from jinja2 import Template
from jinja2 import Environment, FileSystemLoader
from markupsafe import escape
from view.view import View

from config import settings



class MainPageView(View):
    def __init__(self):
        super().__init__()

    def get_page(self) -> str:
        tm = self.env.get_template('main_page.htm')
        return tm.render()
