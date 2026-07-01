class minStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, item):
        self.stack.append(item)
        if not self.min_stack or item <= self.min_stack[-1]:
            self.min_stack.append(item)
    
    def pop(self):
        if not self.stack:
            raise IndexError("pop from empty stack")
        item = self.stack.pop()
        if item == self.min_stack[-1]:
            self.min_stack.pop()
    
    def get_min(self):
        if not self.min_stack:
            raise IndexError("get_min from empty stack")
        return self.min_stack[-1]

    def is_empty(self):
        return len(self.stack) == 0
    
    def peek(self):
        if not self.stack:
            raise IndexError("peek from empty stack")
        return self.stack[-1]

