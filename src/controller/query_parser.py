import re

class QueryParser:
    def __init__(self, query: str): # query in format "key1=val1&key2=val2&...&keyN=valN".
        self.query:str = query
        self.parse_query()
        
    def parse_query(self) -> None:
        self.divide_by_ampersand()
        self.divide_by_equal_sign()
        
    def divide_by_ampersand(self) -> None:
        self.key_value_in_rows: list[str] = re.split('&', self.query)

    def divide_by_equal_sign(self) -> None:
        if self.query == '':
            self.parsed_query = {}
            return
        
        self.parsed_query: dict[str, str] = {}
        for key_value_row in self.key_value_in_rows:
            if key_value_row.count('=') != 1:
                continue
            key, value = re.split('=', key_value_row)
            if key == '':
                continue
            self.parsed_query[key.strip()] = value.strip()

    def to_dict(self) -> dict[str, str]:
        return self.parsed_query
