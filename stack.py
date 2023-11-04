class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

    def size(self):
        return len(self.items)
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print("Stack:", stack.items)
print("Size:", stack.size())
print("Peek:", stack.peek())

popped_item = stack.pop()
print("Popped:", popped_item)

print("Stack after pop:", stack.items)
