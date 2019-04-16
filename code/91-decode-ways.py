def numDecodings(s):
    if not s:
        return 0

    CODE1 = map(str, range(1,10))
    CODE2 = map(str, range(10,27))

    l = len(s)
    ways = [0 for _ in range(l+1)]
    ways[0] = 1

    if s[0] in CODE1:
        ways[1] = 1

    for i in range(1,l):
        if s[i] in CODE1:
            ways[i+1] += ways[i]
        if s[i-1:i+1] in CODE2:
            ways[i+1] += ways[i-1]

    return ways[-1]
