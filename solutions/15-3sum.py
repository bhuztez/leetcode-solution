"""
>>> threeSum([-1, 0, 1, 2, -1, -4])
[[-1, -1, 2], [-1, 0, 1]]
"""

from nsum import enumerate_t, comb2, dict_add_by_distance, get_all_pairs, indices_to_num

def threeSum(num):
    target = 0
    d = {}
    num1 = list(enumerate_t(num))
    num2 = comb2(num1)
    dict_add_by_distance(d, num1, target)
    dict_add_by_distance(d, num2, target)
    return map(list, frozenset(indices_to_num(get_all_pairs(d,target,3),num)))
