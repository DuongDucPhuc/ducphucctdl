

class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
        
    def enqueue(self, value):
        self.items.append(value)
        return "the element is ínerted at the end of Queue"
    
    def peek(self):
        if self.isEmoty():
            return "The is not any alement in the Queue"
        else:
            return self.items[0]
        
    def delete(self):
        self.items = None


customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.peek())
customQueue.delete()