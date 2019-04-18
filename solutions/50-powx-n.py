from digit import int2digits
from iterator import izip

def square(x):
    while True:
        yield x
        x *= x

def pow(x, n):
    r = 1.0

    if n < 0:
        x = 1.0/x
        n = -n

    for a, b in izip(square(x), int2digits(n, 2)):
        if b:
            r *= a

    return r
