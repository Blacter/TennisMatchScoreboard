from pprint import pprint

# from sqlalchemy.orm import DeclarativeBase
# from sqlalchemy.orm import Mapped
# from sqlalchemy.orm import mapped_column
# from sqlalchemy import String

# class Base(DeclarativeBase):
#     pass

from config import settings
from tennis_match_scoreboard import TennisMatchScoreboard

if __name__ == '__main__':
    tennis_match_scoreboard: TennisMatchScoreboard = TennisMatchScoreboard(settings.SERVER_HOST, settings.SERVER_PORT)
    tennis_match_scoreboard.start_server()

