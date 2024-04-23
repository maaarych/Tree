class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def pre_order(node):
    if node is None:
        return []
    return [node.data] + pre_order(node.left) + pre_order(node.right)


def in_order(node):
    if node is None:
        return []
    return in_order(node.left) + [node.data] + in_order(node.right)


def post_order(node):
    if node is None:
        return []
    return post_order(node.left) + post_order(node.right) + [node.data]




a = Node("A")
b = Node("B")
c = Node("C")
a.left = b
a.right = c
d = Node("D")
c.left = d
print(pre_order(a))  # ['A', 'B', 'C', 'D']
print(in_order(a))  # ['B', 'A', 'D', 'C']
print(post_order(a))  # ['B', 'D', 'C', 'A']
