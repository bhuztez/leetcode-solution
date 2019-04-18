def list_inplace_remove(l, p):
    i = 0

    for j in range(0, len(l)):
        if p(l[j]):
            continue

        l[i] = l[j]
        i += 1

    return i
