def depth(tree):
    if tree is None:
        return 0
    else:
        ld = depth(tree.left)
        rd = depth(tree.right)
        assert -2 < ld - rd < 2
        return max(ld,rd)+1
    
def isBalanced(root):
    try:
        depth(root)
        return True
    except AssertionError:
        return False
