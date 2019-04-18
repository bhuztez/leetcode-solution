def int2digits(x, base=10):
    while x:
        yield x%base
        x //= base

def digits2int_b(it, base=10):
    i = 0
    for d in it:
        i = i * base + d
    return i

def digits2int_l(it, base=10):
    r = 0
    for i, d in enumerate(it):
        r += d * (base ** i)
    return r

def add_by_digit(it, base=10):
    c = 0
    for a, b in it:
        r = a+b+c
        yield r%base
        c = r//base
    if c > 0:
        yield c

def roman_int_map():
    return (
        ( 'M', 1000),
        ('CM',  900),
        ( 'D',  500),
        ('CD',  400),
        ( 'C',  100),
        ('XC',   90),
        ( 'L',   50),
        ('XL',   40),
        ( 'X',   10),
        ('IX',    9),
        ( 'V',    5),
        ('IV',    4),
        ( 'I',    1))

def _int2roman(n):
    for r, i in roman_int_map():
        yield r*(n//i)
        n = n%i

def int2roman(n):
    return "".join(_int2roman(n))

def _roman2int(s):
    for r, i in roman_int_map():
        while s.startswith(r):
            yield i
            s = s[len(r):]

def roman2int(s):
    return sum(_roman2int(s))
