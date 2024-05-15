class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class caynhiphan:
    def __init__(self):
        self.root = None
    def kiemtracaynhiphan(self,node):
        if node is None:
            return True