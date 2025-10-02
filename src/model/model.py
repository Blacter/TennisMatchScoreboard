from sqlalchemy import create_engine

from config import settings

class Model:
    def __init__(self):
        self.engine = create_engine(url = settings.DATABASE_URL_pymysql, echo = True)
        