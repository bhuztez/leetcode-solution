def anagrams(strs):
    d = {}
    for s in strs:
        k = "".join(sorted(s))
        d[k] = d.get(k, []) + [s]
    return sum([v for k,v in d.items() if len(v) > 1], [])
