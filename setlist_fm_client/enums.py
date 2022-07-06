from enum import Enum


class Accept(Enum):
    xml = "application/xml"
    json = "application/json"


class Sort(Enum):
    sort_name = "sortName"
    relevance = "relevance"
