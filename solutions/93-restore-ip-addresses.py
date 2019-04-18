def next_state(c, states):
    for ints,remain in states:
        new_remain = remain+c
        new_int = int(new_remain)
        if new_int < 256 and remain != "0":
            new_ints = ints + [new_int]
            if len(new_ints) < 5:
                yield new_ints, ""

        if len(new_remain) < 4 and remain != "0":
            yield ints, new_remain


def restoreIpAddresses(s):
    states = [([], "")]

    for c in s:
        states = list(next_state(c, states))

    return [".".join(map(str,ints))
            for (ints,remain) in states
            if remain == "" and len(ints) == 4]
