from number import overflow32
from digit import digits2int_b


def iter_digit(s):
    for c in s:
        if not c.isdigit():
            return
        yield int(c)


def myAtoi(str):
    s = str.strip()
    if not s:
        return 0

    if s[0] in '-+':
        sign = {'-':-1,'+':1}[s[0]]
        s = s[1:]
    else:
        sign = 1

    n = sign * digits2int_b(iter_digit(s))
    return overflow32(n)
