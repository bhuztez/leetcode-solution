from misc import find_word_ranges

def wordBreak(s, dict):
    paths = [path for seg in dict for path in find_word_ranges(seg, s)]
    paths.sort()

    reachable = [False for _ in range(len(s)+1)]
    reachable[0] = True

    for b,e in paths:
        reachable[e] |= reachable[b]

    return reachable[-1]
