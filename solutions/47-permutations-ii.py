from combinatorics import perm


def permuteUnique(num):
    num.sort()
    return map(list, perm(num, len(num)))
