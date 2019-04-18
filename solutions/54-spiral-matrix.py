from misc import spiral


def spiralOrder(matrix):
    if not matrix:
        return []

    return [
        matrix[y][x]
        for x, y in spiral(True, 0, 0, len(matrix[0]), len(matrix))]
