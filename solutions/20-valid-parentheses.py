def isValid(s):
    PAIR = {")":"(", "}":"{","]":"["}
    stack = []

    for c in s:
        if c in "])}":
            if not stack or stack.pop() != PAIR[c]:
                return False
        else:
            stack.append(c)

    return False if stack else True
