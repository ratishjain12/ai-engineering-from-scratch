class Queue:
    def __init__(self, size=None):
        self.items = []
        self.size = size

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        if self.size is not None:
            return len(self.items) >= self.size
        return False

    def enqueue(self, item):
        if not self.is_full():
            self.items.append(item)
        else:
            raise IndexError("enqueue to full queue")

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from empty queue")
    
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("peek from empty queue")