"""
>>> solveNQueens(4)
[['..Q.', 'Q...', '...Q', '.Q..'], ['.Q..', '...Q', 'Q...', '..Q.']]
"""

from algorithm_x import select, solve


def is_primary(k):
    n, _ = k
    return (n == "x") or (n == "y")


def make_chess_board(s, n):
    board = [
        ["." for _ in range(n)]
        for _ in range(n) ]
    for x, y in s:
        board[y][x] = "Q"
    return map("".join, board)


def solveNQueens(n):
    cols = (
        [ ("x", x) for x in range(n) ] +
        [ ("y", y) for y in range(n) ] +
        [ ("c", c) for c in range(2*n-1) ] +
        [ ("d", d) for d in range(-n+1,n) ]
    )

    Cols = {c:set() for c in cols}

    Rows = {
        (x,y): [("x", x), ("y", y), ("c", x+y), ("d", x-y)]
        for x in range(n)
        for y in range(n)}

    for r, cols in Rows.iteritems():
        for c in cols:
            Cols[c].add(r)

    return [
        make_chess_board(s, n)
        for s in solve(Cols, Rows, [], is_primary)]
