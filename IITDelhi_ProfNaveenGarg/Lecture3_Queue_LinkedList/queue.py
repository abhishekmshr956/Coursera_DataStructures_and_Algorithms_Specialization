class Queue:

    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def enqueue(self, element : object) -> None:
        self.items.append(element)

    def dequeue(self) -> object:
        if self.isEmpty():
            raise IndexError("Queue is empty")
        else:
            return self.items.pop(0)
        
    def front(self) -> object:
        if self.isEmpty():
            raise IndexError("Queue is empty")
        else:
            return self.items[0]
        
    def __repr__(self):
        return str(self.items)
        
if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(10)
    queue.enqueue(15)
    print(queue)
    queue.dequeue()
    queue.front()