from digit import add_by_digit
from iterator import izip_longest

def plusOne(digits):
    l = list(add_by_digit(izip_longest(digits[::-1], [1], fill=0)))
    return l[::-1]
