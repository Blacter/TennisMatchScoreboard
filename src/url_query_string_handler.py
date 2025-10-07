from copy import copy
import re
        

class UrlQueryStringHandler:
    def __init__(self, query_string: str) -> None:        
        self.query_string: str = query_string
        self.parse_query_string() 
    
    def parse_query_string(self) -> None:
        self.divide_by_ampersand()
        # print(f'{self.key_value_in_rows = }')
        self.divide_by_equal_sign()       
    
    def divide_by_ampersand(self) -> None:
        self.key_value_in_rows: list[str] = re.split('&', self.query_string)
        
    def divide_by_equal_sign(self) -> None:
        if self.query_string == '':
            self.parsed_query = {}
            return
        
        self.parsed_query: dict[str, str] = {}
        for key_value_row in self.key_value_in_rows:
            if key_value_row.count('=') != 1:
                continue
            key, value = re.split('=', key_value_row)
            if key == '':
                continue
            self.parsed_query[key] = value
            
    def get_query_string_in_dict_format(self) -> dict[str, str]:
        return copy(self.parsed_query)
            
    
if __name__ == '__main__':
    # query_string: str = 'key1=val1&key2=val2&key3=val3'
    # query_string: str = 'key1=val1&key2=val2'
    # query_string: str = 'key1=val1'
    # query_string: str = 'key1=val1&' # <- error
    # query_string: str = '&key1=val1'
    # query_string: str = 'key1=val1=123&key1=val1'
    query_string: str = 'key1=val1&123&key1&=val1'
    # query_string: str = ''
    
    url_query_string_handler: UrlQueryStringHandler = UrlQueryStringHandler(query_string)
    
    print(url_query_string_handler.get_query_string_in_dict_format())
    