def search_range(start, end):
    return (start, end)


def search_range_size(r):
    start, end = r
    return end-start


def search_range_midpoint(r):
    start, end = r
    return (start+end-1) // 2


def search_range_left(r, midpoint):
    start, _ = r
    return (start, midpoint)


def search_range_right(r, midpoint):
    _, end = r
    return (midpoint+1, end)


def binary_search(l, cmp, r=None):
    if not callable(cmp):
        cmp = cmp.__cmp__

    if r is None:
        r = search_range(0, len(l))

    while search_range_size(r) > 0:
        m = search_range_midpoint(r)

        if cmp(l[m]) > 0:
            r = search_range_right(r, m)
        elif cmp(l[m]) < 0:
            r = search_range_left(r, m)
        elif cmp(l[m]) == 0:
            break
    else:
        return r

    rl = search_range_left(r, m+1)
    rr = search_range_right(r, m-1)

    while search_range_size(rl) > 0:
        m = search_range_midpoint(rl)

        if cmp(l[m]) > 0:
            rl = search_range_right(rl, m)
        elif cmp(l[m]) == 0:
            rl = search_range_left(rl, m)

    while search_range_size(rr) > 0:
        m = search_range_midpoint(rr)

        if cmp(l[m]) < 0:
            rr = search_range_left(rr, m)
        elif cmp(l[m]) == 0:
            rr = search_range_right(rr, m)

    return search_range(rl[0], rr[0])
