class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        current = self.head

        while current.next:
            current = current.next
        current.next = node
        node.prev = current
    
    def prepend(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        node.next = self.head
        self.head.prev = node
        self.head = node
    
    def delete(self,data):
        if not self.head:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next
    
    def display(self):
        current  = self.head
        while current:
            print(current.data, end = " <->")
            current = current.next
        print("None")


my_list = DoublyLinkedList()

my_list.append(1)
my_list.append(2)       
my_list.append(3)
my_list.display()  # Output: 1 <-> 2 <-> 3 <