def spiral(first, x, y, m, n):
    if m == 0 or n == 0:
        return

    if first:
        for i in range(x,x+m):
            yield i, y

        for i in range(y+1,y+n):
            yield x+m-1, i

        for c in spiral(False, x, y+1, m-1, n-1):
            yield c
    else:
        for i in range(x+m-1,x-1,-1):
            yield i, y+n-1

        for i in range(y+n-2,y-1,-1):
            yield x, i

        for c in spiral(True, x+1, y, m-1, n-1):
            yield c


def merge_intervals(intervals):
    last = intervals[0]

    for c in intervals[1:]:
        if last[1] >= c[0]:
            last[1] = max(c[1], last[1])
        else:
            yield last
            last = c

    yield last


def find_word_ranges(word, s):
    start = 0
    l = len(word)

    while True:
        try:
            index = s.index(word, start)
        except ValueError:
            break

        yield (index, index+l)
        start = index + 1


def iter_palindrome(s):
    l = len(s)

    for i in range(l):
        for j in range(i+1, l+1):
            w = s[i:j]
            if w == w[::-1]:
                yield i, j
