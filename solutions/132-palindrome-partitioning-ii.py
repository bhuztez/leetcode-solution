from misc import iter_palindrome


def minCut(s):
    steps = [None for _ in range(len(s)+1)]
    steps[0] = 0

    for b, e in iter_palindrome(s):
        if steps[e] is None or steps[b] + 1 < steps[e]:
            steps[e] = steps[b] + 1

    return steps[-1] - 1
