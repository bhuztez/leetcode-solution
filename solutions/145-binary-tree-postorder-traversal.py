def traverse(tree):
    if tree is not None:
        for i in traverse(tree.left):
            yield i
        for i in traverse(tree.right):
            yield i
        yield tree.val


def postorderTraversal(root):
    return list(traverse(root))
