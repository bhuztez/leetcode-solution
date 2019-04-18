"""
>>> searchRange([5, 7, 7, 8, 8, 10], 8)
[3, 4]
"""

from binary_search import search_range_size, binary_search


def searchRange(A, target):
    r = binary_search(A, target)

    if search_range_size(r) <= 0:
        return [-1, -1]

    a, b = r
    return [a, b-1]
