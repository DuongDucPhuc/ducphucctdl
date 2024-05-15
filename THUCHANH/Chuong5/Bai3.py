class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class caynhiphan:
    def __init__(self):
        self.root = None
    def sonutla(self, node):
        if node is None:
            return 0
        elif node.left is None and node.right is None:
            return 1
        else:
            return  self.sonutla(node.left)+self.sonutla(node.right)
tree = caynhiphan()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
print(tree.sonutla(tree.root))       