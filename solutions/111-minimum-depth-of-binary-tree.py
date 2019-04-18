def smaller(l):
    l = [e for e in l if e > 0]
    if len(l):
        return min(l)
    return 0


def minDepth(root):
    if root is None:
        return 0

    return smaller([minDepth(root.left), minDepth(root.right)], 0)+1
