from binary_tree import iter_level

def connect(root):
    for level in iter_level([root]):
        for a, b in zip(level, level[1:]+[None]):
            a.next = b
