"""
>>> jump([2,3,1,1,4])
2
"""

def jump(A):
    steps = [None for _ in A]
    steps[0] = 0
    last = len(A) - 1

    max_reachable = 0

    for i in range(0, last):
        if steps[i] is None:
            continue

        reachable = min(i+A[i], last)

        if reachable <= max_reachable:
            continue

        for j in range(max_reachable+1, reachable+1):
            steps[j] = steps[i] + 1

        max_reachable = reachable

    return steps[-1]
