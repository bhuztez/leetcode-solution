def validate(tree):
    if tree is None:
        return
    
    if tree.left:
        lmin, lmax = validate(tree.left)
        assert tree.val > lmax
    else:
        lmin = tree.val
        
    if tree.right:
        rmin, rmax = validate(tree.right)
        assert tree.val < rmin
    else:
        rmax = tree.val
        
    return (lmin, rmax)


def isValidBST(root):
    try:
        validate(root)
        return True
    except AssertionError:
        return False
