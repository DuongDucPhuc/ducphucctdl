class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class caynhiphan:
    def __init__(self):
        self.root = None
    def sonuttrunggian(self, node):
        if node is None:
            return 0
        elif node.left is not None and node.right is not None:
            return 0
        elif node.left:
            return self.sonuttrunggian(node.left)
        else:
            return self.sonuttrunggian(node.right)
tree = caynhiphan()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.left.left = Node(4)
tree.root.right = Node(3)
tree.root.right.right = Node(5)
print(tree.sonuttrunggian(tree.root))
    