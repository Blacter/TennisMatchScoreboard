class RequestBodyException(Exception):
    def __init__(self, description):
        self.description: str = description

    def __str__(self):
        return f'RequestBodyException: {self.description}'
    