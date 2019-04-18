from iterator import izip

def canCompleteCircuit(gas, cost):
    change = [(g-c) for g, c in izip(gas, cost)]
    total = 0
    stops = len(change)
    l, r = 0, 0

    while True:
        while True:
            total += change[r]
            r = (r + 1) % stops

            if total < 0:
                break

            if l == r:
                return l

        while total < 0:
            total -= change[l]
            l += 1

            if l == stops:
                return -1
