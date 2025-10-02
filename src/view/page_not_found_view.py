from view.view import View


class PageNotFoundView(View):
    def get_page(self) -> str:
        tm = self.env.get_template('page_not_found_page.htm')
        return tm.render()
