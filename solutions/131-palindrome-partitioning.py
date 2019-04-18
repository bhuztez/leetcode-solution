from misc import iter_palindrome


def iter_segs(n, parents):
    if n == 0:
        yield ()
    else:
        for p in parents[n]:
            for seg in iter_segs(p, parents):
                yield seg + ((p, n),)


def partition(s):
    parents = [[] for _ in range(len(s)+1)]
    parents[0] = []

    for b, e in iter_palindrome(s):
        parents[e].append(b)

    return [[s[a:b] for (a,b) in seg]
            for seg in iter_segs(len(s), parents)]
