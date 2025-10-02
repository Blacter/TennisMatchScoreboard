from copy import copy
import re
from markupsafe import escape
import urllib

type PostBodyDict = dict[str, str] | None


from controller.post_body.post_body_error import BodySizeTooLarge

class PostRequestBodyHandler:
    def __init__(self, post_request_body: bytes, post_request_body_length: int):
        if post_request_body_length > 1000 or len(post_request_body) > 1000:
            raise BodySizeTooLarge()
        
        self.post_request_body: bytes = post_request_body        
        
        self.transform_body_in_string_format()
        self.process_string_input_by_user()
        self.parse_to_key_value_dict()
    
    def transform_body_in_string_format(self) -> None:
        self.post_body_string: str = self.post_request_body.decode('utf-8')
    
    def process_string_input_by_user(self) -> None:
        self.post_body_string = self.post_body_string[0:256]
        self.post_body_string = self.post_body_string.strip()
        self.post_body_string = urllib.parse.unquote(self.post_body_string)
        # self.post_body_string = escape(self.post_body_string)

    def parse_to_key_value_dict(self) -> dict[str, str]:
        print(f'{self.post_body_string=}')
        key_value_list: list[str] = self.post_body_string.split('&')
        self._parameters_dict: dict[str, str] = {}

        for key_value in key_value_list:
            key, value = key_value.split('=')
            self._parameters_dict[key] = value.strip()

    def is_key_in_body(self, key: str) -> bool:
        if key in self._parameters_dict.keys():
            return True
        return False

    def get_body_in_dict_format(self) -> PostBodyDict:
        return copy(self._parameters_dict)

    @staticmethod
    def could_str_be_parsed_to_float(value: str) -> bool:
        return re.match(r'^\d+\.\d+$', value)        
    