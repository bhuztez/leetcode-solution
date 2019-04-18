"""
>>> A = [1,1,2]
>>> removeDuplicates(A)
2
>>> A[:2]
[1, 2]
"""

from inplace import list_inplace_remove


def if_duplicate():
    last = yield
    curr = yield False

    while True:
        next = yield (curr == last)
        last, curr = curr, next


def removeDuplicates(A):
    p = if_duplicate()
    next(p)
    return list_inplace_remove(A, p.send)
