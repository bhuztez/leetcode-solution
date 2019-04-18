"""
>>> minWindow("ADOBECODEBANC", "ABC")
'BANC'
"""

def minWindow(S, T):
    need = {}

    for c in T:
        need[c] = need.get(c, 0) + 1

    l, r = 0, 0
    min_range = None
    min_length = None

    while True:
        while r < len(S):
            c = S[r]

            if c in need:
                need[c] -= 1

            r += 1

            if all((v<=0) for v in need.itervalues()):
                break
        else:
            break

        while l < r:
            c = S[l]

            if c in need:
                if need[c] == 0:
                    break

                need[c] += 1

            l += 1

        if min_range is None or r -l < min_length:
            min_length = r - l
            min_range = l, r

        c = S[l]
        need[c] += 1
        l += 1

    if min_range is None:
        return ""

    l, r = min_range
    return S[l:r]
