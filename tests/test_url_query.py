import pytest

from controller.url.url_query import UrlQuery

class TestUrlQuery:
    @pytest.mark.parametrize(
        'query_string, result_query_dict',
        [
            ('key1=val1&key2=val2&key3=val3', {'key1':'val1', 'key2':'val2', 'key3':'val3'}), 
            ('key1=val1&key2=val2', {'key1':'val1','key2':'val2'}),
            ('key1=val1',  {'key1':'val1'}),
            # ('key1=val1&', {}), # <- error
            # ('&key1=val1', {}),
            # ('key1=val1=123&key1=val1', {}),
            # ('key1=val1&123&key1&=val1', {}),
            ('', {}),
        ]
    )
    def test_query_parse(self, query_string: str, result_query_dict: dict[str, str]) -> None:
        url_query: UrlQuery = UrlQuery(query_string)
        assert url_query.to_dict() == result_query_dict
        