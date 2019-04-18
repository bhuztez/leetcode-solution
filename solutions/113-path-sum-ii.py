from binary_tree import iter_path

def pathSum(root, s):
    return [list(p) for p in iter_path(root) if sum(p) == s]
