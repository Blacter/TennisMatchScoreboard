import os

from jinja2 import Template
from jinja2 import Environment, FileSystemLoader
from markupsafe import escape
from view.view import View

from config import settings
from typealiases import HtmlPage


class MainPageView(View):
    def __init__(self):
        super().__init__()

    def get_page(self) -> HtmlPage:
        tm = self.env.get_template('main_page.html')
        return tm.render(static_files_path=self.static_files_path)
