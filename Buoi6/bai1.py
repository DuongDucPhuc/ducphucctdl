class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class linkedlist:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
a  = linkedlist(10)
print(a.head.value)