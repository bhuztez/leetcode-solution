def generate(numRows):
    if numRows == 0:
        return []
    if numRows == 1:
        return [[1]]

    rows = [[1]]

    for i in range(2,numRows+1):
        rows.append([1] + [rows[-1][j-1]+rows[-1][j] for j in range(1, i-1)] + [1])

    return rows
