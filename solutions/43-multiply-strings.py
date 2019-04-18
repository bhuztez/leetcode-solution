def multiply(num1, num2):
    O = ord('0')
    r = [0 for _ in range(len(num1)*len(num2)+1) ]

    for i, x in enumerate(num1[::-1]):
        for j, y in enumerate(num2[::-1]):
            r[i+j] += (ord(x) - O) * (ord(y) - O)

    for i in range(len(r)-1):
        r[i+1] += r[i] // 10
        r[i] %= 10

    r.reverse()
    return "".join(chr(O+c) for c in r).lstrip('0') or '0'
