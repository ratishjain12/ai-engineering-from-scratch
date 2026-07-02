class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.items = [None] * size
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.front == self.rear and self.items[self.front] is None

    def is_full(self):
        return self.front == self.rear and self.items[self.front] is not None

    def enqueue(self, item):
        if self.is_full():
            raise IndexError("Queue is full")

        self.items[self.rear] = item
        self.rear = (self.rear + 1) % self.size

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        item = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.size
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        return self.items[self.front]

    def display(self):
        print(self.items)


# Example
q = CircularQueue(4)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

q.display()
# [10, 20, 30, 40]

print(q.dequeue())   # 10
print(q.dequeue())   # 20

q.display()
# [None, None, 30, 40]

q.enqueue(50)
q.enqueue(60)

q.display()
# [50, 60, 30, 40]

print(q.peek())      # 30

while not q.is_empty():
    print(q.dequeue(), end=" ")

# Output:
# 30 40 50 60