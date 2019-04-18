from binary_tree import iter_path

def hasPathSum(root, s):
    return any((sum(p) == s) for p in iter_path(root))
