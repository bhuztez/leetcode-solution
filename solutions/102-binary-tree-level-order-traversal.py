from binary_tree import iter_level

def levelOrder(root):
    return [[node.val for node in nodes]
            for nodes in iter_level([root])]
