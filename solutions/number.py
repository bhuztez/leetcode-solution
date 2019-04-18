def sign(x):
    return -1 if x<0 else 1


def overflow32(x, pos=2147483647, neg=-2147483648):
    if x < -2147483648:
        return neg
    elif x > 2147483647:
        return pos
    else:
        return x
