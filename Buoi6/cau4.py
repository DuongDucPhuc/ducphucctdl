# cau4
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def update_head(self, new_node):
        self.head = new_node
# Tạo danh sách liên kết
llist = LinkedList()
llist.push(5)
llist.push(40)
llist.push(60)
llist.push(80)
new_node = Node(500)
llist.update_head(new_node)
# In danh sách liên kết
temp = llist.head
while (temp):
    print(temp.data, end=" ")
    temp = temp.next