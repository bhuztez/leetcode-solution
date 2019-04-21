from combinatorics import c

def numTrees(n):
    return c(2*n, n)//(n+1)
