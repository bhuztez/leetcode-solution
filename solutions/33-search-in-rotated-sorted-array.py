from binary_search import search_range, search_range_size, binary_search


def search(A, target):
    if len(A) == 0:
        return -1

    s = 1
    while s < len(A):
        if A[s] != A[0]:
            break
        s += 1

    e = len(A)
    while e > s:
        if A[e-1] != A[0]:
            break
        e -= 1

    r = binary_search(A, lambda x: -1 if x<A[0] else 1, search_range(s,e))

    if target >= A[0]:
        r = binary_search(A, target, search_range(s-1, r[0]))
    elif target < A[0]:
        r = binary_search(A, target, search_range(r[0], e))

    if search_range_size(r) <= 0:
        return -1

    return r[0]
