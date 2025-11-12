from whitenoise import WhiteNoise

from config import settings
from tennis_match_scoreboard import TennisMatchScoreboard

tennis_match_scoreboard: TennisMatchScoreboard = TennisMatchScoreboard(settings.SERVER_HOST, settings.SERVER_PORT)
application = WhiteNoise(tennis_match_scoreboard, root=r"..")

wsgi_app = application.application

if __name__ == '__main__':
    wsgi_app.start_server()
    # application.application.start_server()
    