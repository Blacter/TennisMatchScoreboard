from markupsafe import escape
import os
from pprint import pprint
import sys
from whitenoise import WhiteNoise


from waitress import serve


from controller.controller import Controller
from controller.post_body.post_request_body_handler import PostRequestBodyHandler
from controller.main_page_controller import MainPageController
from controller.match_score_controller import MatchScoreController
from controller.match_score_post_controller import MatchScorePostController
from controller.matches_controller import MatchesController
from controller.new_match_controller import NewMatchController
from controller.new_match_create_controller import NewMatchCreateController
from controller.page_not_found_controller import PageNotFoundController
from controller.response import Response
from controller.url.url_query import UrlQuery
from controller.url.url_path import UrlPath
from model.model import Model
from model.new_match_model import NewMatchModel
from typealiases import PostRequestBodyDict
from typealiases import ResponseHeaders
from view.main_page_view import MainPageView
from view.new_match_view import NewMatchView


class TennisMatchScoreboard:
    def __init__(self, host, port) -> None:
        self.host: str = host
        self.port: str = port

    def start_server(self) -> None:
        print(f'Server started at {self.host}:{self.port}')
        application = WhiteNoise(self.simple_app, root=self.get_root_directory())
        serve(application, host=self.host, port=self.port)
        
    @staticmethod
    def get_root_directory() -> str:
        return os.path.split(os.path.dirname(os.path.abspath(sys.argv[0])))[0]
        
    @staticmethod
    def debug_output():
        pass

    @staticmethod
    def simple_app(environ, start_response) -> list:        
        url_path: UrlPath = UrlPath(environ['PATH_INFO'])
        url_query: UrlQuery = UrlQuery(environ['QUERY_STRING'])
        query_dict: dict[str, str] = url_query.to_dict()
        post_body: dict[str, str] = TennisMatchScoreboard.get_post_request_body(environ)
        
        # TennisMatchScoreboard.debug_output(environ, post_body)
        
        if url_path.is_in_main_directory() and TennisMatchScoreboard.is_get_request_method(environ):
            main_page_controller: MainPageController = MainPageController()
            response: Response = main_page_controller.get_response()
        elif url_path.is_in_new_match_directory() and TennisMatchScoreboard.is_get_request_method(environ):
            new_match_controller: NewMatchController = NewMatchController()
            response: Response = new_match_controller.get_response()
        elif url_path.is_in_new_match_directory() and TennisMatchScoreboard.is_post_request_method(environ):
            create_new_match_controller: NewMatchCreateController = NewMatchCreateController(post_body) # post_body
            response: Response = create_new_match_controller.get_response()
        elif url_path.is_in_match_score_directory() and TennisMatchScoreboard.is_get_request_method(environ):
            match_score_controller: MatchScoreController = MatchScoreController(query_dict)
            response: Response = match_score_controller.get_response()
        elif url_path.is_in_match_score_directory() and TennisMatchScoreboard.is_post_request_method(environ):
            match_score_controller: MatchScoreController = MatchScorePostController(query_dict, post_body)
            response: Response = match_score_controller.get_response()
        elif url_path.is_in_matches_directory() and TennisMatchScoreboard.is_get_request_method(environ):
            matches_controller: MatchesController = MatchesController(query_dict)
            response: Response = matches_controller.get_response()
        else:
            page_not_found_controller: PageNotFoundController = PageNotFoundController()
            response: Response = page_not_found_controller.get_response()

        status = response.code     
        start_response(status, response.headers)

        return [(response.body + '\n').encode('UTF-8')]    

    @staticmethod
    def get_post_request_body(environ) -> PostRequestBodyDict:
        post_body: PostRequestBodyDict = {}
        if environ['REQUEST_METHOD'] == 'POST':
            post_body_raw = next(environ['wsgi.input'])
            content_length: int = int(environ['CONTENT_LENGTH'])
            post_body_request_handler = PostRequestBodyHandler(post_body_raw, content_length)
            post_body = post_body_request_handler.to_dict()  
            # print('post_body_dict:')          
            # pprint(post_body)
        return post_body
    
    @staticmethod
    def is_get_request_method(environ) -> bool:
        return environ['REQUEST_METHOD'] == 'GET'
    
    @staticmethod
    def is_post_request_method(environ) -> bool:
        return environ['REQUEST_METHOD'] == 'POST'
    
    i: int = 0
    @staticmethod
    def debug_output(environ, post_body: PostRequestBodyDict) -> None:
        print('Start' + str(TennisMatchScoreboard.i) + '-'*20)
        TennisMatchScoreboard.i += 1
        pprint(environ)
        print('* ' * 20)        
        print('WSGI.ERRORS: ')         
        print(f'{environ["wsgi.errors"]=}')
        print('* ' * 20)

        print('post_body:')
        pprint(post_body)
        print('End ' + '-'*20)
                    