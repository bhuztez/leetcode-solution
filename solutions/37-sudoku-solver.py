from algorithm_x import select, solve


def solveSudoku(board):
    cols = (
        [ ("rc", j, i) for i in range(1,10) for j in range(1,10)] +
        [ ("rn", i, j) for i in range(1,10) for j in range(1,10)] +
        [ ("cn", i, j) for i in range(1,10) for j in range(1,10)] +
        [ ("bn", i, j) for i in range(1,10) for j in range(1,10)])

    rows = [ (j,i,k) for i in range(1,10) for j in range(1,10) for k in range(1,10) ]

    Rows = {}

    for x,y,n in rows:
        Rows[(x,y,n)] = [("rc",x,y), ("rn", x,n), ("cn", y,n), ("bn", 1+(x-1)//3+(y-1)//3*3, n)]

    Cols = {c:set() for c in cols}

    for r, cols in Rows.iteritems():
        for c in cols:
            Cols[c].add(r)

    for y, line in enumerate(board):
        for x, n in enumerate(line):
            if n != '.':
                select(Cols, Rows, (x+1,y+1,int(n)))

    for s in solve(Cols, Rows, []):
        for x,y,n in s:
            board[y-1][x-1] = str(n)
        break
