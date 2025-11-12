from typealiases import HtmlPage
from view.view import View


class NewMatchView(View):
    def get_page(self, is_error: bool = False, error_description: str = '') -> HtmlPage:
        tm = self.env.get_template('new_match_page.html')
        return tm.render(
            static_files_path=self.static_files_path,
            is_error=is_error,
            error_description=error_description)
    