class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n


def tree_by_levels(node):
    result=[]
    if node is None:
        return []
    l_node = [node]
    while l_node:
        current = l_node.pop(0)
        result.append(current.value)
        if current.left:
            l_node.append(current.left)
        if current.right:
            l_node.append(current.right)
    return result

print(tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)))