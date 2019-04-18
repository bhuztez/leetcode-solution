def is_mirror(a, b):
    if a is None and b is None:
        return True
    elif a is None or b is None:
        return False
    elif a.val != b.val:
        return False
    else:
        return is_mirror(a.left, b.right) and is_mirror(a.right, b.left)

def isSymmetric(root):
    return root is None or is_mirror(root.left, root.right)
