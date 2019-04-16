"""
>>> convert("PAYPALISHIRING", 3)
'PAHNAPLSIIGYIR'
"""

from iterator import izip

def convert(s, nRows):
    if nRows == 1:
        return s

    n = nRows * 2 - 2
    s += ' ' * (n - len(s) % n)
    l = [s[i::n] for i in range(n)]
    r = l[0]

    for i in range(1, nRows-1):
        r += "".join(a+b for a,b in izip(l[i], l[n-i]))

    r += l[nRows-1]
    return "".join(r.split(" "))
