# 1.ENQUEUE OPERATION
# It adds an element to the end of the queue
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Queue:
# Constructor    
    def __init__(self,value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
# Prints queue
    def print_queue(self):
        if self.length == 0:
            return None
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

my_queue = Queue(1)
my_queue.enqueue(2)
my_queue.print_queue()

# Output
"""

1
2

"""

# 2.DEQUEUE OPERATION
# It removes an element from the start of the queue

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Queue:
    def __init__(self,value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
    def print_queue(self):
        if self.length == 0:
            return None
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
    def dequeue(self):
            if self.length == 0: # if the list is empty, it returns None
                return None
            temp = self.first  # if the list has 2 or more elements, it removes the first element and the first points to the next element to the first
            self.first = self.first.next
            temp.next = None
            self.length -= 1 
            if self.length == 0:  # if the queue has one element, the first and last points to None after dequeue 
                self.last = None  # self.first is already None due to self.first.next
            return temp

my_queue = Queue(1)
my_queue.enqueue(2)
my_queue.print_queue()
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
my_queue.print_queue()

# Output
"""

1
2
<__main__.Node object at 0x0000024963810310>
<__main__.Node object at 0x0000024963810110>
None
None

"""