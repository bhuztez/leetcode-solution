"""
>>> findMedianSortedArrays([1,2], [1,2])
1.5
>>> findMedianSortedArrays([1,2,3], [4,5])
3
"""

from binary_search import (
    search_range,
    search_range_size,
    search_range_midpoint,
    search_range_left,
    search_range_right)


def kth(A, B, k):
    ra = search_range(0, len(A))
    rb = search_range(0, len(B))

    while True:
        if search_range_size(ra) <= 0:
            return B[rb[0]+k]
        if search_range_size(rb) <= 0:
            return A[ra[0]+k]

        ma = search_range_midpoint(ra)
        mb = search_range_midpoint(rb)
        rla = search_range_left(ra, ma)
        rlb = search_range_left(rb, mb)

        if search_range_size(rla)+search_range_size(rlb) < k:
            if A[ma] < B[mb]:
                k -= 1+search_range_size(rla)
                ra = search_range_right(ra, ma)
            else:
                k -= 1+search_range_size(rlb)
                rb = search_range_right(rb, mb)
        else:
            if A[ma] > B[mb]:
                ra = rla
            else:
                rb = rlb


def findMedianSortedArrays(A,B):
    l = len(A) + len(B)
    if l % 2:
        return kth(A, B, l//2)
    else:
        return 0.5 * (kth(A, B, l//2-1) + kth(A, B, l//2))
