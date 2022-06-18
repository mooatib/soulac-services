from pydantic import BaseModel


class Page:
    def __init__(self, nbr, limit, orderBy, orderByAsc, search):
        self.nbr = nbr
        self.limit = limit
        self.orderBy = orderBy
        self.orderByAsc = orderByAsc
        self.search = search

    nbr: int = 0
    limit: int = 10
    orderBy: str = "id"
    orderByAsc: bool = True
    search: str = ""
