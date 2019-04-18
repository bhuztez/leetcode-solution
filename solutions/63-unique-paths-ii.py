def uniquePathsWithObstacles(obstacleGrid):
    g = obstacleGrid
    h = len(g)
    w = len(g[0])

    s = [ [None for _ in range(w)] for _ in range(h)]

    for y in range(h):
        for x in range(w):
            if g[y][x] == 1:
                s[y][x] = 0
            elif x == 0 and y == 0:
                s[y][x] = 1
            elif x == 0:
                s[y][0] = s[y-1][0]
            elif y == 0:
                s[0][x] = s[0][x-1]
            else:
                s[y][x] = s[y-1][x] + s[y][x-1]

    return s[-1][-1]
