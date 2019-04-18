"""
>>> ladderLength("hit", "cog", ["hot","dot","dog","lot","log"])
5
"""

def neighbour(word):
    for n in range(len(word)):
        for c in 'abcdefghijklmnopqrstuvwxyz':
            yield word[:n]+c+word[n+1:]

def ladderLength(start, end, dict):
    visited = set([start])
    remain = set([end])
    remain.update(dict)

    new = [start]
    length = 1

    while end not in visited:
        new = remain.intersection(n for word in new for n in neighbour(word))
        length += 1
        remain.difference_update(new)
        visited.update(new)

        if not new:
            return 0

    return length
