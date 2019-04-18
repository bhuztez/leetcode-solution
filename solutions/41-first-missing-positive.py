def firstMissingPositive(A):
    l = len(A)

    for i in range(l):
        while 0 < A[i] <= l:
            x = A[i] - 1
            if x == i or A[x] == A[i]:
                break
            A[x], A[i] = A[i], A[x]

    for i in range(l):
        if A[i] != i + 1:
            return i + 1

    return l + 1
