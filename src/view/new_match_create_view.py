from view.view import View

class NewMatchCreateView(View):
    def get_page(self) -> str:
        tm = self.env.get_template('new_match_created_page.htm')
        return tm.render(player_1='nickname_1', player_2='nickname_2')
    