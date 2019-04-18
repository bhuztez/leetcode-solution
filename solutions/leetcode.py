def list_node_from_iter(it):
    try:
        e = next(it)
    except StopIteration:
        return None

    root = ListNode(e)
    cur = root
    for e in it:
        node = ListNode(e)
        cur.next = node
        cur = node
    return root


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __iter__(self):
        while self is not None:
            yield self.val
            self = self.next

    @staticmethod
    def from_iter(iterable):
        return list_node_from_iter(iter(iterable))


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
