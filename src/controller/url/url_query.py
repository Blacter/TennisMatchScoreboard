from copy import copy

from controller.query_parser import QueryParser
        

class UrlQuery:
    def __init__(self, query_string: str) -> None:
        query_string: str = query_string
        query_parser: QueryParser = QueryParser(query_string)
        self._query_dict: dict[str, str] = query_parser.to_dict()

    def to_dict(self) -> dict[str, str]:
        return copy(self._query_dict)
            
    
if __name__ == '__main__':
    query_string: str = 'key1=val1&key2=val2&key3=val3'
    # query_string: str = 'key1=val1&key2=val2'
    # query_string: str = 'key1=val1'
    # query_string: str = 'key1=val1&' # <- error
    # query_string: str = '&key1=val1'
    # query_string: str = 'key1=val1=123&key1=val1'
    # query_string: str = 'key1=val1&123&key1&=val1'
    # query_string: str = ''
    
    url_query: UrlQuery = UrlQuery(query_string)
    
    print(url_query.to_dict())
    