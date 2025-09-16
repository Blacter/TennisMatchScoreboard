from pprint import pprint

from waitress import serve

from url_parser import UrlQueryParser

class TennisMatchScoreboard:
    def __init__(self, host, port) -> None:
        self.host: str = host
        self.port: str = port
    
    @staticmethod
    def simple_app(environ, start_response) -> list:
        """
        (dict, callable( status: str,
                        headers: list[(header_name: str, header_value: str)]))
                    -> body: iterable of strings
        """        
        request_uri: str = environ['REQUEST_URI']
        url_query_parser: UrlQueryParser = UrlQueryParser(query_string=environ['QUERY_STRING'])        
        parsed_query: dict[str, str] = url_query_parser.get_parsed_query()
        
        response: str = ''
        print(f'{environ['PATH_INFO'] = }')
        if environ['PATH_INFO'] == '/':
            response = 'main page'
        elif environ['PATH_INFO'] == '/new-match':
            response = 'new match page'
        elif environ['PATH_INFO'] == '/match-score':
            response = 'match score page'
        elif environ['PATH_INFO'] == '/matches':
            response = 'finished matches page'
        else :
            response = 'page not found'
            
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        start_response(status, response_headers)        
        
        return [(response + '\n').encode('UTF-8'), request_uri.encode('UTF-8')]        
    
    def start_server(self) -> None:
        serve(self.simple_app, host=self.host, port=self.port)

    