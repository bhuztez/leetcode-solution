def _maxPathSum(tree):
    if tree is None:
        return (0, 0)

    lpath, lsum = _maxPathSum(tree.left)
    rpath, rsum = _maxPathSum(tree.right)

    max_path = max(lpath+tree.val, rpath+tree.val, tree.val)
    max_sum = max(max_path, lpath+rpath+tree.val)

    max_sum = max(max_sum, lsum) if tree.left else max_sum
    max_sum = max(max_sum, rsum) if tree.right else max_sum
    return (max_path, max_sum)


def maxPathSum(root):
    return _maxPathSum(root)[1]
