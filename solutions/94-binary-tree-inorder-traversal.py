def traverse(tree):
    if tree is not None:
        for i in traverse(tree.left):
            yield i
        yield tree.val
        for i in traverse(tree.right):
            yield i

def inorderTraversal(root):
    return list(traverse(root))
