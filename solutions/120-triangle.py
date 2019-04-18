def minimumTotal(triangle):
    if not triangle:
        return 0

    rows = [triangle[0]]

    for i, r in enumerate(triangle[1:]):
        rows.append([rows[-1][0]+r[0]] + [r[j] + min(rows[-1][j-1], rows[-1][j]) for j in range(1, i+1) ] + [rows[-1][-1]+r[-1]])

    return min(rows[-1])
