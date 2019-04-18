def hasCycle(head):
    h1 = head
    h2 = head

    while True:
        try:
            h1 = h1.next
            h2 = h2.next.next
        except AttributeError:
            return False
        if h1 is h2:
            return True
