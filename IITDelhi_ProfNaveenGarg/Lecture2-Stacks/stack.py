class Stack:

    def __init__(self):
        self.items = []

    def size(self) -> int:
        return len(self.items)
    
    def isEmpty(self) -> bool:
        return len(self.items) == 0
    
    def __repr__(self):
        return str(self.items)
    
    def top(self) -> object:
        # throws StackEmptyException
        if not self.isEmpty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def push(self, element: object) -> None:
        self.items.append(element)

    def pop(self) -> object:
        if not self.isEmpty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")
        
if __name__ == '__main__':
    stack = Stack()
    stack.push(3)
    stack.push(2)
    print(stack)
    stack.pop()
    stack.top()
    stack.pop()
    stack.pop()