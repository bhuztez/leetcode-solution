from iterator import izip
from binary_tree import iter_level


def zigzag():
    while True:
        yield None
        yield -1


def zigzagLevelOrder(root):
    return [[node.val for node in v[::s]]
            for v, s in izip(iter_level([root]), zigzag())]
