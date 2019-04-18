from iterator import izip
from binary_tree import iter_level

def connect(root):
    for level in iter_level([root]):
        for a, b in izip(level, level[1:]+[None]):
            a.next = b
