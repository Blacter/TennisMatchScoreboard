from typealiases import HtmlPage
from view.view import View

class NewMatchCreateView(View):
    def get_page(self) -> HtmlPage:
        tm = self.env.get_template('new_match_created_page.htm')
        return tm.render(
            static_files_path=self.static_files_path,
            player_1='nickname_1',
            player_2='nickname_2')
    