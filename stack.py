class Stack:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def __bool__(self):
        return bool(self.items)

    def clear(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        if not self.items:
            raise IndexError("peek from empty stack")
        return self.items[-1]
