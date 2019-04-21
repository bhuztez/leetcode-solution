from iterator import count, izip
from misc import spiral


def generateMatrix(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    for (x, y), v in zip(spiral(True, 0, 0, n, n), count(1)):
        matrix[y][x] = v

    return matrix
