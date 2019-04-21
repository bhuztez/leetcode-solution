def neighbour(word):
    for n in range(len(word)):
        for c in 'abcdefghijklmnopqrstuvwxyz':
            yield word[:n]+c+word[n+1:]


def iter_paths(n, parents):
    if not parents[n]:
        yield [n]
    else:
        for p in parents[n]:
            for path in iter_paths(p, parents):
                yield path + [n]


def findLadders(start, end, dict):
    visited = set([start])
    remain = set()
    remain.update(dict)
    remain.discard(start)

    new = [start]
    parents = {k: set() for k in [start,end]+list(dict)}

    while end not in visited:
        next_new = []

        for word in new:
            nbs = remain.intersection(neighbour(word))
            next_new.extend(nbs)

            for n in nbs:
                parents[n].add(word)

        new = next_new
        remain.difference_update(new)
        visited.update(new)

        if not new:
            return []

    return list(iter_paths(end, parents))
