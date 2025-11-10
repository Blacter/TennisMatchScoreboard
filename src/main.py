from whitenoise import WhiteNoise

from config import settings
from tennis_match_scoreboard import TennisMatchScoreboard

if __name__ == '__main__':    
    tennis_match_scoreboard: TennisMatchScoreboard = TennisMatchScoreboard(settings.SERVER_HOST, settings.SERVER_PORT)
    application = WhiteNoise(tennis_match_scoreboard, root=r"..")
    application.application.start_server()
    