"""
Queue implementation using LinkedList
The head of the list is the front of the queue, the tail of the list is the rear of the queue
Insert new element at the rear (tail of the list) and remove the element from the front (head of the list)
"""

class Node:

    def __init__(self, data = None):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'<Node: {self.data}>'

class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return data
    
    def front(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.head.data
    
    def __str__(self):
        if self.is_empty():
            return "Queue is empty"
        current = self.head
        queue_str = ""
        while current:
            queue_str += str(current.data) + " "
            current = current.next
        return queue_str.strip()

if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print("Queue:", q)
    print("Dequeue:", q.dequeue())
    print("Front:", q.front())
    print("Queue after dequeue:", q)