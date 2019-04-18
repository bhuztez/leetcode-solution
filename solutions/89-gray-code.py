def grayCode(n):
    if n == 0:
        return [0]

    a = grayCode(n-1)
    m = 1 << (n-1)
    b = [(i|m) for i in a[::-1]]

    return a + b
