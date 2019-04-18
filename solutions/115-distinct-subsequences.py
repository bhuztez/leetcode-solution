def numDistinct(S, T):
    if not S:
        return 0

    state = {T:1}
    count = 0

    for ch in S:
        next_state = {}
        for s,c in state.items():
            if ch == s[0]:
                if s[1:] == "":
                    count += c
                else:
                    next_state[s[1:]] = next_state.get(s[1:], 0)+c

            next_state[s] = next_state.get(s, 0)+c
        state = next_state

    return count
