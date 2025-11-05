from whitenoise import WhiteNoise

from config import settings
from tennis_match_scoreboard import TennisMatchScoreboard

if __name__ == '__main__':
    tennis_match_scoreboard: TennisMatchScoreboard = TennisMatchScoreboard(settings.SERVER_HOST, settings.SERVER_PORT)
    tennis_match_scoreboard.start_server()
    
    tennis_match_scoreboard: TennisMatchScoreboard = TennisMatchScoreboard(settings.SERVER_HOST, settings.SERVER_PORT) # .simple_app
    # application = WhiteNoise(tennis_match_scoreboard, root=r"C:\Users\slawa\Desktop\Python\00.Pet_Projects\07.TennisMatchScoreboard\TennisMatchScoreboard")
    application = WhiteNoise(tennis_match_scoreboard, root=r"..")
    # application.add_files("/path/to/more/static/files", prefix="more-files/")
    # tennis_match_scoreboard.start_server()
    application.application.start_server()
    