import pytest

from service.match_score_service import MatchScoreService


class TestMatchScoreService:
    @pytest.mark.parametrize(
        'score,winner,res_score',
        [
            #
            ('0,0,0:0,0,0','player_1_win','0,0,15:0,0,0'),
            ('0,0,15:0,0,0','player_1_win','0,0,30:0,0,0'),
            ('0,0,30:0,0,0','player_1_win','0,0,40:0,0,0'),
            ('0,0,40:0,0,0','player_1_win','0,1,0:0,0,0'),
            
            ('0,0,0:0,0,0','player_2_win','0,0,0:0,0,15'),
            ('0,0,0:0,0,15','player_2_win','0,0,0:0,0,30'),
            ('0,0,0:0,0,30','player_2_win','0,0,0:0,0,40'),
            ('0,0,0:0,0,40','player_2_win','0,0,0:0,1,0'),
            
            ('0,0,40:0,0,0','player_1_win','0,1,0:0,0,0'),
            ('0,1,40:0,0,0','player_1_win','0,2,0:0,0,0'),
            ('0,2,40:0,0,0','player_1_win','0,3,0:0,0,0'),
            ('0,3,40:0,0,0','player_1_win','0,4,0:0,0,0'),
            ('0,4,40:0,0,0','player_1_win','0,5,0:0,0,0'),
            ('0,5,40:0,0,0','player_1_win','1,0,0:0,0,0'),
            
            ('0,0,0:0,0,40','player_2_win','0,0,0:0,1,0'),
            ('0,0,0:0,1,40','player_2_win','0,0,0:0,2,0'),
            ('0,0,0:0,2,40','player_2_win','0,0,0:0,3,0'),
            ('0,0,0:0,3,40','player_2_win','0,0,0:0,4,0'),
            ('0,0,0:0,4,40','player_2_win','0,0,0:0,5,0'),
            ('0,0,0:0,5,40','player_2_win','0,0,0:1,0,0'),
            ('0,0,0:0,6,40','player_2_win','0,0,0:1,0,0'),
            #
            ('0,0,40:0,0,40','player_1_win','0,0,ad:0,0,40'),
            ('0,0,40:0,0,40','player_2_win','0,0,40:0,0,ad'),            
            ('0,0,ad:0,0,40','player_1_win','0,1,0:0,0,0'),
            ('0,0,ad:0,0,40','player_2_win','0,0,40:0,0,40'),
            ('0,0,40:0,0,ad','player_1_win','0,0,40:0,0,40'),
            ('0,0,40:0,0,ad','player_2_win','0,0,0:0,1,0'),
            #
            ('1,3,40:1,2,30','player_1_win','1,4,0:1,2,0'),
            ('1,2,30:1,3,40','player_2_win','1,2,0:1,4,0'),
            ('0,5,40:1,2,30','player_1_win','1,0,0:1,0,0'),
            ('1,2,30:0,5,40','player_2_win','1,0,0:1,0,0'),
            #
            ('0,6,40:0,5,30','player_1_win','1,0,0:0,0,0'),
            ('0,5,30:0,6,40','player_2_win','0,0,0:1,0,0'),
            #
            ('0,6,7:0,6,6', 'player_1_win', '1,0,0:0,0,0'),
            ('0,6,7:1,6,6', 'player_1_win', '1,0,0:1,0,0'),
            ('1,6,7:0,6,6', 'player_1_win', '2,0,0:0,0,0'),
            ('1,6,7:1,6,6', 'player_1_win', '2,0,0:1,0,0'),
            ('0,6,6:0,6,7', 'player_2_win', '0,0,0:1,0,0'),
            ('1,6,6:0,6,7', 'player_2_win', '1,0,0:1,0,0'),
            ('0,6,6:1,6,7', 'player_2_win', '0,0,0:2,0,0'),
            ('1,6,6:1,6,7', 'player_2_win', '1,0,0:2,0,0'),
            # (',,:,,', 'player__win', ',,:,,')
        ]
    )
    def test_player_win_one_score_base(self, score, winner, res_score):
        match_score_service: MatchScoreService = MatchScoreService(score)
        if winner == 'player_1_win':
            match_score_service.increase_player_one_score_on_one_point()
        elif winner == 'player_2_win':
            match_score_service.increase_player_two_score_on_one_point()
        assert match_score_service.get_match_score_in_str_format() == res_score
        