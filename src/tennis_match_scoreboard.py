from markupsafe import escape
from pprint import pprint

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
from model.model import Model
from model.new_match_model import NewMatchModel
from typealiases import PostBodyDict
from view.main_page_view import MainPageView
from view.new_match_view import NewMatchView
from url_query_string_handler import UrlQueryStringHandler
from url_path_info_handler import UrlPathInfoHandler

# type PostBodyDict = dict[str, str] | None

class TennisMatchScoreboard:
    def __init__(self, host, port) -> None:
        self.host: str = host
        self.port: str = port

    @staticmethod
    def simple_app(environ, start_response) -> list:
        content_length: int
        post_body: PostBodyDict = {}
        post_body_raw: bytes = b''
        post_body_request_handler: PostRequestBodyHandler 
        response_code: int = ''
        response_str: str = ''        
        
        if environ['REQUEST_METHOD'] == 'POST':
            post_body_raw = next(environ['wsgi.input'])
            content_length: int = int(environ['CONTENT_LENGTH'])
            post_body_request_handler = PostRequestBodyHandler(post_body_raw, content_length)
            # post_body: PostBodyDict = PostBodyRequestHandler.get_parsed_post_body(environ['wsgi.input'])
            post_body = post_body_request_handler.get_body_in_dict_format()  
            print('post_body_dict:')          
            pprint(post_body)

        url_path_info_handler: UrlPathInfoHandler = UrlPathInfoHandler(
            environ['PATH_INFO'])
        url_query_string_handler: UrlQueryStringHandler = UrlQueryStringHandler(
            environ['QUERY_STRING'])
        query_string_dict: dict[str, str] = url_query_string_handler.get_query_string_in_dict_format()
        
        TennisMatchScoreboard.debug_output(environ, post_body_raw, post_body)
        
        response_headers = TennisMatchScoreboard.get_default_response_headers()
        
        if url_path_info_handler.is_in_directory('/') and environ['REQUEST_METHOD'] == 'GET':
            main_page_controller: MainPageController = MainPageController()
            response_code, response_str, response_headers = main_page_controller.get_response()
        elif url_path_info_handler.is_in_directory('/new-match') and environ['REQUEST_METHOD'] == 'GET':
            new_match_controller: NewMatchController = NewMatchController()
            response_code, response_str, response_headers = new_match_controller.get_response()
        elif url_path_info_handler.is_in_directory('/new-match') and environ['REQUEST_METHOD'] == 'POST':
            create_new_match_controller: NewMatchCreateController = NewMatchCreateController(post_body) # post_body
            response_code, response_str, response_headers = create_new_match_controller.get_response()
        elif url_path_info_handler.is_in_directory('/match-score') and environ['REQUEST_METHOD'] == 'GET':
            match_score_controller: MatchScoreController = MatchScoreController(query_string_dict)
            response_code, response_str, response_headers = match_score_controller.get_response()
        elif url_path_info_handler.is_in_directory('/match-score') and environ['REQUEST_METHOD'] == 'POST':
            match_score_controller: MatchScoreController = MatchScorePostController(query_string_dict, post_body)
            response_code, response_str, response_headers = match_score_controller.get_response()
        elif url_path_info_handler.is_in_directory('/matches'):
            matches_controller: MatchesController = MatchesController()
            response_code, response_str, response_headers = matches_controller.get_response()
        else:            
            page_not_found_controller: PageNotFoundController = PageNotFoundController()
            response_code, response_str, response_headers = page_not_found_controller.get_response()

        status = response_code
        # response_headers = [('Content-type', 'text/html')]        
        start_response(status, response_headers)

        return [(response_str + '\n').encode('UTF-8')]

    def start_server(self) -> None:
        serve(self.simple_app, host=self.host, port=self.port)
        
    @staticmethod
    def get_default_response_headers() -> list[tuple[str]]:
        return [('Content-type', 'text/html')] 
    
    # def get_redirect_header(target_location_with_parameters: str) -> list[tuple[str]]:
    #     return[('Location', target_location_with_parameters)]
        
    i: int = 0
    @staticmethod
    def debug_output(environ, post_body_raw: str, post_body: PostBodyDict) -> None:
        print('Start' + str(TennisMatchScoreboard.i) + '-'*20)
        TennisMatchScoreboard.i += 1
        pprint(environ)
        print('* ' * 20)        
        print('WSGI.ERRORS: ')         
        print(f'{environ['wsgi.errors']=}')
        
        if environ['REQUEST_METHOD'] == 'POST':            
            print('WSGI.INPUT: ')
            print(f'{post_body_raw=}')
        print('* ' * 20)

        print('post_body:')
        pprint(post_body)
        print('End ' + '-'*20)
                    