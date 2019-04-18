"""
>>> searchInsert([1,3,5,6], 5)
2
>>> searchInsert([1,3,5,6], 2)
1
>>> searchInsert([1,3,5,6], 7)
4
>>> searchInsert([1,3,5,6], 0)
0
"""

from binary_search import binary_search


def searchInsert(A, target):
    a, _ = binary_search(A, target)
    return a
