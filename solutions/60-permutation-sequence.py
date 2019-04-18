"""
>>> getPermutation(3, 1)
'123'
>>> getPermutation(3, 2)
'132'
>>> getPermutation(3, 3)
'213'
>>> getPermutation(3, 4)
'231'
>>> getPermutation(3, 5)
'312'
>>> getPermutation(3, 6)
'321'
"""

from combinatorics import perm_k

def getPermutation(n, k):
    return "".join(str(c+1) for c in perm_k(k-1, n))
