from view.view import View

class MatchesView(View):
    def get_page(self) -> str:
        tm = self.env.get_template('matches_page.htm')
        return tm.render()