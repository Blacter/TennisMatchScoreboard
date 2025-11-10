from copy import copy
import re
from markupsafe import escape
import urllib

from typealiases import PostRequestBodyDict
from controller.post_body.post_body_error import BodySizeTooLarge
from controller.query_parser import QueryParser


class PostRequestBodyHandler:
    def __init__(self, post_request_body: bytes, post_request_body_length: int):
        if post_request_body_length > 1000 or len(post_request_body) > 1000:
            raise BodySizeTooLarge()
        
        self.query: str = post_request_body.decode('utf-8')        
        self.process_query_user_input()
        query_parser: QueryParser = QueryParser(self.query)
        self._query_dict: dict[str, str] = query_parser.to_dict()
    
    def process_query_user_input(self) -> None:
        self.query = self.query.strip()
        self.query = self.query[0:256]
        self.query = urllib.parse.unquote(self.query)

    def to_dict(self) -> dict[str, str]:
        return copy(self._query_dict)
    