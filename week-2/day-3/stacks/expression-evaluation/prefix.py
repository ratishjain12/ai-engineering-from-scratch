# stack implementation using python list
class Stack:
    def __init__(self, size = None):
        self.items = []
        self.size = size

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        if self.size is not None:
            return len(self.items) >= self.size
        return False

    def push(self,item):
        if not self.is_full():
            self.items.append(item)
        else:
            raise IndexError("push to full stack")

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


def evaluate_prefix(expression):
    stack = Stack()
    operators = {'+', '-', '*', '/'}

    for char in reversed(expression):
        if char.isdigit():
            stack.push(int(char))
        elif char in operators:
            operand1 = stack.pop()
            operand2 = stack.pop()
            if char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '*':
                result = operand1 * operand2
            elif char == '/':
                result = operand1 / operand2
            stack.push(result)

    return stack.pop()