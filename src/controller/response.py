from copy import deepcopy

from typealiases import ResponseCode
from typealiases import ResponseBody
from typealiases import ResponseHeaders

class Response:
    def __init__(self, code: ResponseCode, body: ResponseBody, headers: ResponseHeaders):
        self._code: ResponseCode = code
        self._body: ResponseBody = body
        self._headers: ResponseHeaders = headers
        
    @property
    def code(self) -> ResponseCode:
        return self._code
    
    @property
    def body(self) -> ResponseBody:
        return self._body
        
    @property
    def headers(self) -> ResponseHeaders:
        return deepcopy(self._headers)
    