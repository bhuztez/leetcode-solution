def p(m,n):
    r = 1
    for i in range(m, m-n, -1):
        r *= i
    return r


def c(m,n):
    return p(m,n)/p(n,n)


def product(*args):
    r = [()]
    for a in args:
        r = [x+(y,) for x in r for y in a]
    return r


def _to_factorial(k, n):
    for i in range(1, n+1):
        yield k % i
        k /= i


def to_factorial(k, n):
    f = list(_to_factorial(k, n))
    f.reverse()
    return f


def _perm_k(k, n):
    f = to_factorial(k, n)
    l = range(n)

    for i in f:
        yield l.pop(i)


def perm_k(k, n):
    return list(_perm_k(k,n))


def perm(l, n):
    if n == 0:
        yield ()

    for i in range(len(l)):
        if i > 0 and l[i] == l[i-1]:
            continue

        for p in perm(l[:i]+l[i+1:], n-1):
            yield (l[i],) + p


def comb(l, n):
    if n == 0:
        yield ()
    else:
        for i in range(len(l)):
            if i > 0 and l[i] == l[i-1]:
                continue

            for r in comb(l[i+1:], n-1):
                yield (l[i],) + r


def next_permutation(lst):
    length = len(lst)

    if length <= 1:
        return lst

    for k in range(length-1, 0, -1):
        if lst[k-1] < lst[k]:
            break
    else:
        return lst[::-1]

    l = k
    k -= 1

    for m in range(l+1, length):
        if lst[k] < lst[m]:
            l = m

    lst[k], lst[l] = lst[l], lst[k]
    lst[k+1:] = lst[:k:-1]
    return lst
