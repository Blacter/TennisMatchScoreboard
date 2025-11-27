from typing import TypeAlias

HtmlPage: TypeAlias = str
PostRequestBodyDict: TypeAlias = dict[str, str] | None
ResponseCode: TypeAlias = str
ResponseBody: TypeAlias = str
ResponseHeaders: TypeAlias = list[tuple[str]]
