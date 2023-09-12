class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None
    
    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if self.is_empty():
            raise Exception("List is empty")
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
        
        raise Exception(f"{data} not found in the list") # optional
    
    def __str__(self):
        if self.is_empty():
            return "List is empty"
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        return ' -> '.join(map(str, elements))
    
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.prepend(0)
    linked_list.append(3)

    print("Linked List:", linked_list)  # Output: Linked List: 0 -> 1 -> 2 -> 3

    linked_list.delete(1)
    linked_list.delete(0)

    print("Linked List after deletion:", linked_list)  # Output: Linked List after deletion: 2 -> 3

        