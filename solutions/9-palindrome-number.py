from digit import int2digits, digits2int_b

def isPalindrome(x):
    if x < 0:
        return False
    return x == digits2int_b(int2digits(x))
