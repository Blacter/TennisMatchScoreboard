class QueryStringException(Exception):
    def __init__(self, description: str):
        self.description: str = description
        
    def __str__(self) -> str:
        return f'QueryStringException: {self.description}'
    