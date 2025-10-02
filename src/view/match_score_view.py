from view.view import View


class MatchScoreView(View):
    def get_page(self) -> str:
        tm = self.env.get_template('match_score_page.htm')
        return tm.render()
