from misc import find_word_ranges

def iter_segs(n, parents):
    if n == 0:
        yield ()
    else:
        for p in parents[n]:
            for seg in iter_segs(p, parents):
                yield seg + ((p, n),)

def wordBreak(s, dict):
    paths = [path for seg in dict for path in find_word_ranges(seg, s)]
    paths.sort()

    if not any(b==0 for b,_ in paths):
        return []

    if not any(e==len(s) for _,e in paths):
        return []

    parents = [[] for _ in range(len(s)+1)]
    parents[0] = []

    for b,e in paths:
        parents[e].append(b)

    return [" ".join(s[a:b] for (a,b) in seg)
            for seg in iter_segs(len(s), parents)]
