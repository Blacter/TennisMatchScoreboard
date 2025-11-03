from typealiases import HtmlPage
from view.view import View

class MatchesView(View):
    def get_page(self, page_number: str, filter_by_player_name: str, matches: list[dict]) -> HtmlPage:
        tm = self.env.get_template('matches_page.html')
        return tm.render(page_number = page_number, filter_by_player_name = filter_by_player_name, matches=matches)