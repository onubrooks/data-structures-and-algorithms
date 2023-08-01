def traverse(node):
    tree = {
        'value': node.value
    }
    tree.left = traverse(node.left ) if node.left else None
    tree.right = traverse(node.right) if node.right else None
    return tree