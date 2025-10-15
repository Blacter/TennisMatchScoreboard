from config import settings


class UrlPath:
    def __init__(self, path_info: str):
        self.path_info: str = path_info

    def is_in_main_directory(self) -> bool:
        return self.is_in_directory(settings.MAIN_PAGE_PATH)
    
    def is_in_new_match_directory(self) -> bool:
        return self.is_in_directory(settings.NEW_MATCH_PAGE_PATH)
    
    def is_in_match_score_directory(self) -> bool:
        return self.is_in_directory(settings.MATCH_SCORE_PAGE_PATH)
    
    def is_in_matches_directory(self) -> bool:
        return self.is_in_directory(settings.MATCHES_PAGE_PATH)

    def is_in_directory(self, directory) -> bool:
        return directory == self.path_info
