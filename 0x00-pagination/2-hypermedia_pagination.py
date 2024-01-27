#!/usr/bin/env python3
""" This module contains index_range function and class server"""


import csv
import math
from typing import List, Dict, Optional


def index_range(page, page_size):
    """returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for
    those particular pagination parameters."""

    return (page_size * (page - 1), page_size * page)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """gets the data of the specified page"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        result = []
        dataset = self.dataset()
        if len(dataset) >= page * page_size:
            starting_page = index_range(page, page_size)[0]
            ending_page = index_range(page, page_size)[1] + 1
            result = [dataset[i] for i in range(starting_page, ending_page)]

        return result

    def get_hyper(self, page: int = 1,
                  page_size: int = 10) -> Dict[str, Optional[int]]:
        """gets the data cridentials"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = len(self.dataset())
        total_pages = math.ceil(dataset / page_size)

        return {
            "page_size": len(self.get_page(page, page_size)),
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": page + 1 if page * page_size < dataset else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
