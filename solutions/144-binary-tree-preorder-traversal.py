def traverse(tree):
    if tree is not None:
        yield tree.val
        for i in traverse(tree.left):
            yield i
        for i in traverse(tree.right):
            yield i

def preorderTraversal(root):
    return list(traverse(root))
