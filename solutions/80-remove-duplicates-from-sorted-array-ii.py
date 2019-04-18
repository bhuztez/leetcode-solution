"""
>>> A = [1,1,1,2,2,3]
>>> removeDuplicates(A)
5
>>> A[:5]
[1, 1, 2, 2, 3]
"""

from inplace import list_inplace_remove


def if_duplicate2():
    last1 = yield
    last2 = yield False
    curr  = yield False

    while True:
        next = yield (curr == last1 == last2)
        last1, last2, curr = last2, curr, next


def removeDuplicates(A):
    p = if_duplicate2()
    next(p)
    return list_inplace_remove(A, p.send)
