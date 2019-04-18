from digit import add_by_digit
from iterator import imap, izip_longest

def addBinary(a, b):
    l = list(
        imap(
            str,
            add_by_digit(
                izip_longest(
                    imap(int, a[::-1]),
                    imap(int, b[::-1]),
                    fill=0),
            base=2)))
    return "".join(l[::-1])
