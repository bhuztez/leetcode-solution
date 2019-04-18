def iter_level(nodes):
    nodes = [node for node in nodes
             if node is not None]

    while nodes:
        yield nodes
        nodes = [ subnode
                  for node in nodes
                  for subnode in [node.left, node.right]
                  if subnode is not None]


def iter_path(tree, path=()):
    if tree is None:
        return

    path += (tree.val,)

    if tree.left is None and tree.right is None:
        yield path
    else:
        for p in iter_path(tree.left, path):
            yield p

        for p in iter_path(tree.right, path):
            yield p
