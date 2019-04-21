"""
>>> fourSum([1, 0, -1, 0, -2, 2], 0)
[[-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2]]
"""
from nsum import enumerate_t, comb2, dict_add_by_distance, get_all_pairs, indices_to_num

def fourSum(num, target):
    d = {}
    num1 = list(enumerate_t(num))
    num2 = comb2(num1)
    dict_add_by_distance(d, num2, target)
    return list(map(list, frozenset(indices_to_num(get_all_pairs(d,target,4),num))))
