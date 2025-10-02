class UrlPathInfoHandler:
    def __init__(self, path_info: str):
        self.path_info: str = path_info

    def is_in_directory(self, directory) -> bool:
        return directory == self.path_info
