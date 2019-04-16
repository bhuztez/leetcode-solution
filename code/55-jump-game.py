"""
>>> canJump([2,3,1,1,4])
True
>>> canJump([3,2,1,0,4])
False
"""

def canJump(A):
    reach = [False for _ in A]
    reach[0] = True
    last = len(A) - 1

    max_reachable = 0

    for i in range(0, last):
        if not reach[i]:
            continue

        reachable = min(i+A[i], last)

        if reachable <= max_reachable:
            continue

        for j in range(max_reachable+1, reachable+1):
            reach[j] = True

        max_reachable = reachable

    return reach[-1]
