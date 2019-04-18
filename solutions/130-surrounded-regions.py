def neighbours(pos):
    x, y = pos
    yield (x-1, y)
    yield (x, y-1)
    yield (x+1, y)
    yield (x, y+1)


def solve(board):
    if not board:
        return

    w = len(board[0])
    h = len(board)

    pos = set((x,y)
           for y in range(h)
           for x in range(w)
           if board[y][x] == 'O')

    queue = [(x,y)
            for x, y in pos
            if x == 0 or x + 1 == w or y == 0 or y + 1 == h]

    visited = set(queue)

    while queue:
        p = queue.pop()
        for n in neighbours(p):
            if n in pos and n not in visited:
                queue.append(n)
                visited.add(n)

    pos.difference_update(visited)

    for x, y in pos:
        board[y][x] = 'X'
