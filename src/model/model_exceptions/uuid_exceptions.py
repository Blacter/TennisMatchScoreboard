class UuidException(Exception):
    def __str__(self):
        return "Sorry, the match with such uuid does not exist"
    