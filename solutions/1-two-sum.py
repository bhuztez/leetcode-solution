"""
>>> twoSum([2, 7, 11, 1], 9)
(1, 2)
"""

from nsum import enumerate_t, dict_add_by_distance, get_all_pairs

def twoSum(num, target):
    d = {}
    dict_add_by_distance(d, enumerate_t(num), target)
    return list(frozenset(get_all_pairs(d, target, 2)))[0]
