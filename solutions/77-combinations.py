from combinatorics import comb

def combine(n, k):
    return map(list, comb(range(1,n+1), k))
