from linked_list import list_node_to_iter, list_node_from_iter
from iterator import reverse_by_n

def swapPairs(head):
    return list_node_from_iter(reverse_by_n(list_node_to_iter(head), 2))
