#!/usr/bin/env python3
"""Tthis module contains index_range function"""


def index_range(page, page_size):
    """returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for
    those particular pagination parameters."""

    return (page_size * (page - 1), page_size * page)
