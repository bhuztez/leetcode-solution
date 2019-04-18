def detectCycle(head):
    h1 = head
    h2 = head

    while True:
        try:
            h1 = h1.next
            h2 = h2.next.next
        except AttributeError:
            return None

        if h1 is h2:
            break

    h1 = head
    while h1 is not h2:
        h1 = h1.next
        h2 = h2.next

    return h1
