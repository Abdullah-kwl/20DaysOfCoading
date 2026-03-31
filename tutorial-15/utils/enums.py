from enum import Enum

class SortField(str, Enum):
    age = "age"
    name = "name"

class Section(str, Enum):
    A = "A"
    B = "B"
    C = "C"

class SortOrder(str, Enum):
    asc = "asc"
    desc = "desc"