def longestValidParentheses(s):
    PAIR = {")":"(", "}":"{","]":"["}
    pstack = []
    lstack = []

    longest = 0
    current = 0

    for c in s:
        if c in "])}":
            if not pstack or pstack.pop() != PAIR[c]:
                longest = max(current, longest)
                pstack = []
                lstack = []
                current = 0
            else:
                last = lstack.pop()
                current = current + last + 2
                longest = max(current, longest)
        else:
            pstack.append(c)
            lstack.append(current)
            current = 0

    longest = max(current, longest)
    return longest
