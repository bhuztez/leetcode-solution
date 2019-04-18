from binary_tree import iter_level

def levelOrderBottom(root):
    return [[node.val for node in nodes]
            for nodes in iter_level([root])][::-1]
