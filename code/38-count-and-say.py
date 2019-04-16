"""
>>> countAndSay(1)
'1'
>>> countAndSay(2)
'11'
>>> countAndSay(3)
'21'
>>> countAndSay(4)
'1211'
>>> countAndSay(5)
'111221'
"""


def count_and_say(s):
    last = s[0]
    count = 1

    for c in s[1:]:
        if c == last:
            count += 1
        else:
            yield (last, count)
            last = c
            count = 1

    yield (last, count)


def countAndSay(n):
    s = '1'
    for i in range(1, n):
        s = "".join("%d%s"%(r,c) for c, r in count_and_say(s))
    return s
