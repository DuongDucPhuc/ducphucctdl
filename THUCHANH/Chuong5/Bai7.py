class Node:
    def __init__(self, value):
        self.info = value
        self.left = None
        self.right = None

class CayNhiPhan:
    def __init__(self):
        self.root = None

    def SaoChepCay(self, node):
        if node is None:
            return None
        else:
            new_node = Node(node.info)
            new_node.left = self.SaoChepCay(node.left)
            new_node.right = self.SaoChepCay(node.right)
            return new_node

    def InOrder(self, node):
        if node:
            self.InOrder(node.left)
            print(node.info, end=" ")
            self.InOrder(node.right)
tree = CayNhiPhan()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

saochep_tree = CayNhiPhan()
saochep_tree.root = saochep_tree.SaoChepCay(tree.root)
saochep_tree.InOrder(saochep_tree.root)
