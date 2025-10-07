from view.view import View


class ErrorPageView(View):
    def get_page(self, error_description: str) -> str:
        tm = self.env.get_template('error_page.htm')
        return tm.render(error_description=error_description)
