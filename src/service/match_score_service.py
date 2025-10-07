class MatchScoreService:
    def __init__(self, match_score_row: str):
        self.parse_match_score_row(match_score_row)        
        
    def parse_match_score_row(self, match_score_row: str) -> None:
        player_one_score, player_two_score = match_score_row.split(':')
        self.player_one_sets, self.player_one_games, self.palyer_one_points = map(int, player_one_score.split(','))
        self.player_two_sets, self.player_two_games, self.palyer_two_points = map(int, player_two_score.split(','))
        
        
    def increase_player_one_score_on_one_point(self) -> None:
        self.palyer_one_points += 1
        
    def increase_player_two_score_on_one_point(self) -> None:
        self.palyer_two_points += 1
    
    def get_match_score_in_str_format(self) -> str:
        return f'{self.player_one_sets},{self.player_one_games},{self.palyer_one_points}:{self.player_two_sets},{self.player_two_games},{self.palyer_two_points}'
    
    def to_dict(self):
        score_dict = {}
        score_dict['player_1_sets'] = self.player_one_sets
        score_dict['player_1_games'] = self.player_one_games
        score_dict['player_1_points'] = self.palyer_one_points
        score_dict['player_2_sets'] = self.player_two_sets
        score_dict['player_2_games'] = self.player_two_games
        score_dict['player_2_points'] = self.palyer_two_points
        return score_dict    
