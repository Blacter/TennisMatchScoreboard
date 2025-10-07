class DBException(Exception):
    def __str__(self):
        return "Sorry, the service is temporary unavilable"