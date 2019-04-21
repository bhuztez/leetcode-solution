from leetcode import RandomListNode as Node

def copyRandomList(head):
    if head is None:
        return None

    h = head
    d = {}
    while h is not None:
        d[h] = Node(h.label)
        h = h.next

    h = head
    while h is not None:
        if h.next is None:
            d[h].next = None
        else:
            d[h].next = d[h.next]

        if h.random is None:
            d[h].random is None
        else:
            d[h].random = d[h.random]

        h = h.next

    return d[head]
