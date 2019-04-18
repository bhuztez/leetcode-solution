def singleNumber(A):
    x = 0
    for i in A:
        x ^= i
    return x
