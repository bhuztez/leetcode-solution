from combinatorics import perm


def permute(num):
    num.sort()
    return map(list, perm(num, len(num)))
