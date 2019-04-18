from binary_search import search_range, search_range_size, binary_search


def findMin(num):
    s = 1
    while s < len(num):
        if num[s] != num[0]:
            break
        s += 1

    e = len(num)
    while e > s:
        if num[e-1] != num[0]:
            break
        e -= 1

    r = binary_search(num, lambda x: -1 if x<num[0] else 1, search_range(s,e))

    if search_range_size(r) <= 0:
        if r[0] == e:
            return num[0]
        return num[r[0]]

    return num[r[0]]
