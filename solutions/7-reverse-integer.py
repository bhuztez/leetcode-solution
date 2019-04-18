"""
>>> reverse(123)
321
>>> reverse(-123)
-321
"""

from number import sign, overflow32
from digit import int2digits, digits2int_b


def reverse(x):
    n = sign(x) * digits2int_b(int2digits(abs(x)))
    return overflow32(n, 0, 0)
