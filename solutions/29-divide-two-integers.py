from number import sign, overflow32


def divide_step(a, b, s):
    if (a > b):
        q, a = divide_step(a, b << 1, s << 1)
    else:
        q = 0

    if a >= b:
        return (q|s), a - b
    else:
        return q, a


def divide(dividend, divisor):
    s = sign(dividend) * sign(divisor)
    q, r = divide_step(abs(dividend), abs(divisor), 1)
    return overflow32(s*q)
