# 1.PUSH OPERATION
# Pushes an elements at the top of the stack

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Stack:
# Constructor
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
# Prints stack
    def print_stack(self):
        if self.height == 0:
            return None
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

my_stack = Stack(1)
my_stack.push(3)
my_stack.print_stack()

# Output
"""

3
1

"""

# 2.POP OPERATION
# Pops an element from the top of the stack

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Stack:
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    def print_stack(self):
        if self.height == 0:
            return None
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
    def pop(self):
            if self.height == 0: # if the stack is empty, it returns None
                return None
            temp = self.top  # if the stack has 2 or more elements, it removes the top element and the top points to the next element to the top
            self.top = self.top.next
            temp.next = None
            self.height -= 1 
            return temp
    
my_stack = Stack(1)
my_stack.push(2)
my_stack.print_stack()
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.print_stack())

# Output
"""

2
1
<__main__.Node object at 0x000002815A82C190>
<__main__.Node object at 0x000002815A82C390>
None
None

"""