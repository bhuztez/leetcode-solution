def _flatten(tree, n):
    if tree is None:
        return n

    n = _flatten(tree.right, n)
    n = _flatten(tree.left, n)
    tree.left = None
    tree.right = n
    return tree

def flatten(root):
    _flatten(root, None)
