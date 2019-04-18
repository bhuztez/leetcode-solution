from combinatorics import comb

def subsetsWithDup(S):
    S.sort()
    return [list(c) for i in range(len(S)+1) for c in comb(S, i)]
