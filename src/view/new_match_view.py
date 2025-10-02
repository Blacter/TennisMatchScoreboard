from view.view import View


class NewMatchView(View):
    def get_page(self, is_error: bool = False, error_description: str = '') -> str:
        tm = self.env.get_template('new_match_page.htm')
        return tm.render(is_error=is_error, error_description=error_description)