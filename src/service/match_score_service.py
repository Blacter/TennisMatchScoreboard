class MatchScoreService:
    def __init__(self, match_score_raw: str):
        self.parse_match_score_raw(match_score_raw)
        self.reset_score_calculation_state()    
        
    def parse_match_score_raw(self, match_score_row: str) -> None:
        player_one_score, player_two_score = match_score_row.split(':')
        self.player_one_sets, self.player_one_games, self.player_one_points = player_one_score.split(',')
        self.player_two_sets, self.player_two_games, self.player_two_points = player_two_score.split(',')
        self.player_one_sets = int(self.player_one_sets)
        self.player_one_games = int(self.player_one_games)
        self.player_two_sets = int(self.player_two_sets)
        self.player_two_games = int(self.player_two_games)
        
    def reset_score_calculation_state(self) -> None:
        self.is_tie_break = False
        self.player_one_win: bool = False
        self.should_add_set_player_one: bool = False
        self.player_two_win: bool = False
        self.should_add_set_player_two: bool = False
        
    def increase_player_one_score_on_one_point(self) -> None:
        self.identify_tie_break()
        if not self.is_tie_break:
            self.player_one_add_point()
        else:
            self.player_one_points = int(self.player_one_points)
            self.player_two_points = int(self.player_two_points)
            self.player_one_add_tie_break_point()
                        
        if self.should_add_game_player_one():
            self.player_one_add_game()
            
        if self.should_add_set_player_one:
            self.player_one_add_set()
        
    def identify_tie_break(self) -> None:        
        if self.player_one_games == 6 and self.player_two_games == 6:
            self.is_tie_break = True
        
    def player_one_add_point(self) -> None:
        if self.player_one_points == '0':
            self.player_one_points = '15'
        elif self.player_one_points == '15':
            self.player_one_points = '30'
        elif self.player_one_points == '30':
            self.player_one_points = '40'
        elif self.player_one_points == '40' and self.player_two_points < '40':
            self.player_one_points = '0'
            self.player_two_points = '0'
        elif self.player_one_points == '40' and self.player_two_points == '40':
            self.player_one_points = 'ad'
        elif self.player_one_points == '40' and self.player_two_points == 'ad':
            self.player_two_points = '40'
        elif self.player_one_points == 'ad':
            self.player_one_points = '0'
            self.player_two_points = '0'
            
    def player_one_add_tie_break_point(self) -> None:
        if self.player_one_points < 6:
            self.player_one_points += 1
        elif self.player_one_points - self.player_two_points >= 1:
            self.player_one_points = '0'
            self.player_two_points = '0'        

    def player_one_add_game(self) -> None:
        if self.player_one_games < 5:
            self.player_one_games += 1
        elif self.player_one_games - self.player_two_games >= 1 or self.is_tie_break_finished():
            self.player_one_games = 0
            self.player_two_games = 0
            self.should_add_set_player_one: bool = True
        else:
            self.player_one_games += 1
            
    def is_tie_break_finished(self) -> bool:
        return self.player_one_games == 6 and self.player_one_games == 6

    def player_one_add_set(self) -> None:
        if self.player_one_sets == 0:
            self.player_one_sets = 1
        else:
            self.player_one_sets = 2
            self.player_one_win = True

    def player_one_add_match(self) -> None:
        self.player_one_win = True
        
    def should_add_game_player_one(self) -> bool:
        return self.player_one_points == '0' and self.player_two_points == '0'
    
    def increase_player_two_score_on_one_point(self) -> None:
        self.identify_tie_break()
        if not self.is_tie_break:
            self.player_two_add_point()
        else:
            self.player_one_points = int(self.player_one_points)
            self.player_two_points = int(self.player_two_points)
            self.player_two_add_tie_break_point()
                        
        if self.should_add_game_player_two():
            self.player_two_add_game()
            
        if self.should_add_set_player_two:
            self.player_two_add_set()   
        
    def player_two_add_point(self) -> None:
        if self.player_two_points == '0':
            self.player_two_points = '15'
        elif self.player_two_points == '15':
            self.player_two_points = '30'
        elif self.player_two_points == '30':
            self.player_two_points = '40'
        elif self.player_two_points == '40' and self.player_one_points < '40':
            self.player_one_points = '0'
            self.player_two_points = '0'
            # self.player_two_win_game()
        elif self.player_two_points == '40' and self.player_one_points == '40':
            self.player_two_points = 'ad'
        elif self.player_two_points == '40' and self.player_one_points == 'ad':
            self.player_one_points = '40'
        elif self.player_two_points == 'ad':
            self.player_one_points = '0'
            self.player_two_points = '0'
            # self.player_two_win_game()
            
    def player_two_add_tie_break_point(self) -> None:
        if self.player_two_points < 6:
            self.player_two_points += 1
        elif self.player_two_points - self.player_one_points >= 1:
            self.player_one_points = '0'
            self.player_two_points = '0'
    
    def player_two_add_game(self) -> None:
        if self.player_two_games < 5:
            self.player_two_games += 1
        elif self.player_two_games - self.player_one_games >= 1 or self.is_tie_break_finished():
            self.player_one_games = 0
            self.player_two_games = 0
            self.should_add_set_player_two: bool = True
        else:
            self.player_two_games += 1

    def player_two_add_set(self) -> None:
        if self.player_two_sets == 0:
            self.player_two_sets = 1
        else:
            self.player_two_sets = 2
            self.player_two_win = True

    def player_two_add_match(self) -> None:
        self.player_two_win = True
    
    def should_add_game_player_two(self) -> None:
        return self.player_one_points == '0' and self.player_two_points == '0'
    
    def get_match_score_in_str_format(self) -> str:
        return f'{self.player_one_sets},{self.player_one_games},{self.player_one_points}:{self.player_two_sets},{self.player_two_games},{self.player_two_points}'
    
    def to_dict(self):
        score_dict = {}
        score_dict['player_1_sets'] = self.player_one_sets
        score_dict['player_1_games'] = self.player_one_games
        score_dict['player_1_points'] = self.player_one_points
        score_dict['player_2_sets'] = self.player_two_sets
        score_dict['player_2_games'] = self.player_two_games
        score_dict['player_2_points'] = self.player_two_points
        return score_dict    
