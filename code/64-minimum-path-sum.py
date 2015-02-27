def minPathSum(grid):
    g = grid
    h = len(g)
    w = len(g[0])

    s = [ [0 for _ in xrange(w)] for _ in xrange(h)]

    for y in xrange(h):
        for x in xrange(w):
            if x == 0 and y == 0:
                s[0][0] += g[0][0]
            elif x == 0:
                s[y][0] = s[y-1][0] + g[y][0]
            elif y == 0:
                s[0][x] = s[0][x-1] + g[0][x]
            else:
                s[y][x] = min(s[y-1][x], s[y][x-1]) + g[y][x]

    return s[-1][-1]
