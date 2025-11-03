from typealiases import HtmlPage
from view.view import View


class PageNotFoundView(View):
    def get_page(self) -> HtmlPage:
        tm = self.env.get_template('page_not_found_page.html')
        return tm.render()
