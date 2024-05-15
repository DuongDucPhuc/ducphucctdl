class Node:
    def __init__(self, value):
        self.info = value
        self.left = None
        self.right = None

class CayNhiPhan:
    def __init__(self):
        self.root = None
    def sosanhhaicaynhiphan(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        elif node1 is None and node2 is not None:
            return False
        elif node1 is not None and node2 is None:
            return False
        elif node1 != node2:
            return False
        if self.sosanhhaicaynhiphan(node1.left) == self.sosanhhaicaynhiphan(node2.left) and self.sosanhhaicaynhiphan(node1.right) == self.sosanhhaicaynhiphan(node2.right):
            return True
        else:
            return False
cay1 = CayNhiPhan()
cay1.root = Node(1)
cay1.root.left = Node(2)
cay1.root.right = Node(3)

cay2 = CayNhiPhan()
cay2.root = Node(1)
cay2.root.left = Node(2)
cay2.root.right = Node(3)
