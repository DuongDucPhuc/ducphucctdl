class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class linkedlist:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def append(self, value):
        new_done = Node(value)
        self.tail.next = new_done
        self.tail = new_done
        self.length += 1
    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
a = linkedlist(10)
a.append(20)
a.append(30)
a.display()
