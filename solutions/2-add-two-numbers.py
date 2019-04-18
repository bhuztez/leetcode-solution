"""
>>> list(addTwoNumbers(*map(ListNode.from_iter, [[2,4,3],[5,6,4]])))
[7, 0, 8]
"""

from leetcode import ListNode
from iterator import izip_longest
from digit import add_by_digit
from linked_list import list_node_to_iter, list_node_from_iter

def addTwoNumbers(l1, l2):
    return list_node_from_iter(
        add_by_digit(
            izip_longest(
                *map(list_node_to_iter, [l1,l2]),
                fill=0)))
