from typealiases import HtmlPage
from view.view import View


class MatchScoreView(View):
    def get_page(self, player_1_name: str, player_2_name: str, score: dict, winner: str) -> HtmlPage:
        tm = self.env.get_template('match_score_page.htm')
        return tm.render(player_1_name=player_1_name, player_2_name=player_2_name, score=score, winner=winner)
