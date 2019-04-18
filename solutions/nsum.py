from combinatorics import comb

def enumerate_t(it):
    for i, e in enumerate(it):
        yield (i+1,), e

def comb2(num):
    for (i1,n1), (i2,n2) in comb(num, 2):
        yield i1+i2, n1+n2

def dict_append(d, k, v):
    d[k] = d.get(k, []) + [v]

def dict_add_by_distance(d, it, target):
    for e in it:
        dict_append(d, abs(2*e[1]-target), e)

def find_pairs(l, target, sz):
    if len(l) <= 1:
        return

    smaller = [i for i,n in l if 2*n <= target ]
    bigger = [i for i,n in l if 2*n >= target ]

    for i in smaller:
        for j in bigger:
            if len(i)+len(j) != sz:
                continue
            e = i+j
            if len(frozenset(e)) != sz:
                continue
            yield tuple(sorted(e))

def get_all_pairs(d, target, sz):
    for l in d.itervalues():
        for e in find_pairs(l, target, sz):
            yield e

def indices_to_num(it, num):
    for e in it:
        yield tuple(sorted([num[i-1] for i in e]))
