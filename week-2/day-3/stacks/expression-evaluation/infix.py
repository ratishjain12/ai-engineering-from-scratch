# Stack implementation using python list
class Stack:
    def __init__(self, size=None):
        self.items = []
        self.size = size

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        if self.size is not None:
            return len(self.items) >= self.size
        return False

    def push(self, item):
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


def evaluate_infix(expression):
    operands = Stack()
    operators = Stack()

    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    def apply_operator():
        op = operators.pop()
        b = operands.pop()
        a = operands.pop()

        if op == '+':
            operands.push(a + b)
        elif op == '-':
            operands.push(a - b)
        elif op == '*':
            operands.push(a * b)
        elif op == '/':
            operands.push(a / b)

    for char in expression:

        if char == ' ':
            continue

        if char.isdigit():
            operands.push(int(char))

        elif char == '(':
            operators.push(char)

        elif char == ')':
            while operators.peek() != '(':
                apply_operator()
            operators.pop()      # Remove '('

        else:  # operator
            while (not operators.is_empty() and
                   operators.peek() != '(' and
                   precedence[operators.peek()] >= precedence[char]):
                apply_operator()

            operators.push(char)

    while not operators.is_empty():
        apply_operator()

    return operands.pop()


print(evaluate_infix("2+3*4"))      # 14
print(evaluate_infix("(2+3)*4"))    # 20
print(evaluate_infix("8/2+3"))      # 7.0