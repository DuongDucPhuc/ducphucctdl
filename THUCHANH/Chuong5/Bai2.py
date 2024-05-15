class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class caynhiphan:
    def __init__(self):
        self.root = None
    def chieucaocay(self, node):
        if node is None:
            return 0
        else:
            return self.chieucaocay(node.left)+self.chieucaocay(node.right)+1
tree = caynhiphan()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
print(tree.chieucaocay(tree.root))

