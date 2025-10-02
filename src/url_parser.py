import re

type QueryDict = dict[str, str]
        

class UrlQueryParser:
    def __init__(self, query_string: str) -> None:        
        self.query_string: str = query_string        
    
    def get_parsed_query(self) -> QueryDict | None:
        self.parse_key_value_in_rows()
        print(f'{self.key_value_in_rows = }')
        self.parse_key_value_pairs()
        return self.parsed_query        
    
    def parse_key_value_in_rows(self) -> None:
        self.key_value_in_rows: list[str] = re.split('&', self.query_string)
        
    def parse_key_value_pairs(self) -> None:
        if self.query_string == '':
            self.parsed_query = None
            return
        
        self.parsed_query: dict[str, str] = {}
        for key_value_row in self.key_value_in_rows:
            key, value = re.split('=', key_value_row)
            self.parsed_query[key] = value
            
    
    