from combinatorics import c


def uniquePaths(m, n):
    return c(n+m-2, m-1)
