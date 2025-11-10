class BodySizeTooLarge(Exception):
    def __str__(self) -> str:
        return 'Error: body size to large, should be less then 1000 symbols'
