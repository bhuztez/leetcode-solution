def maxDepth(root):
    if root is None:
        return 0
        
    return max(maxDepth(root.left), maxDepth(root.right))+1
