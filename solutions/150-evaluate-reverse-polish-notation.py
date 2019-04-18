from digit import digits2int_b

def evalRPN(tokens):
    OPS = {
        "+": lambda a,b: a+b,
        "-": lambda a,b: a-b,
        "*": lambda a,b: a*b,
        "/": lambda a,b: -(-a/b) if (a*b)<0 else a/b
    }

    stack = []
    for token in tokens:
        if token not in OPS:
            stack.append(int(token))
        else:
            stack = stack[:-2] + [OPS[token](stack[-2], stack[-1])]

    return stack[-1]
