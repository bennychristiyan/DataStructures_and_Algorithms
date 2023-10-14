class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

# constructor
class DoublyLinkedlist:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

# 1.PRINT DOUBLY LINKED LIST
# It prints all the elements in the entire Doubly linked list
    def print_list(self):
        if self.length == 0:
            return None
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

# 2.APPEND TO A DOUBLY LINKED LIST
# It adds an element to the end of the Doubly linked list
    def append_to_list(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True  # optional
    
# 3.POP METHOD
# Removes the last element from a Doubly linked list
    def pop(self):
        if self.length == 0: # if the list is empty, it returns None
            return None
        temp = self.tail  
        if self.length == 1:  # if the list has one element, the head and tail points to None after pop 
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev # if the list has 2 or more elements, it removes the last element and the tail points to the second to last element
            self.tail.next = None
            temp.prev = None
        self.length -= 1 
        return temp
    
My_Linked_list = DoublyLinkedlist(1)
My_Linked_list.append_to_list(2)
My_Linked_list.print_list()
print(My_Linked_list.pop())
print(My_Linked_list.pop())
print(My_Linked_list.pop())
print(My_Linked_list.print_list())

# Output
"""

1
2
<__main__.Node object at 0x000001BA22A7F8D0>
<__main__.Node object at 0x000001BA22A7F890>
None
None

"""

# 4.PREPEND METHOD
# It adds an element to the beginning of the Doubly linked list
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
class DoublyLinkedlist:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def print_list(self):
        if self.length == 0:
            return None
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True  # optional

My_Linked_list = DoublyLinkedlist(1)
My_Linked_list.prepend(3)
My_Linked_list.print_list()

# Output
"""

3
1

"""

# 5.POP FIRST METHOD
# Removes the first element from a Doubly linked list
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
class DoublyLinkedlist:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def print_list(self):
        if self.length == 0:
            return None
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def append_to_list(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True 
    def pop_first(self):
        if self.length == 0: # if the list is empty, it returns None
            return None
        temp = self.head
        if self.length == 1:  # if the list has one element, the head and tail points to None after pop 
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next # if the list has 2 or more elements, it removes the first element and the head points to the second element
            self.head.prev = None
            temp.next = None
        self.length -= 1 
        return temp
    
My_Linked_list = DoublyLinkedlist(1)
My_Linked_list.append_to_list(2)
My_Linked_list.print_list()
print(My_Linked_list.pop_first())
print(My_Linked_list.pop_first())
print(My_Linked_list.pop_first())
print(My_Linked_list.print_list())

# Output
"""

1
2
<__main__.Node object at 0x0000013B9DD60C10>
<__main__.Node object at 0x0000013B9DD60A50>
None
None

"""

# 6.GET VALUE METHOD
# Gets a element in the Doubly linked list using index
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
class DoublyLinkedlist:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def append_to_list(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True  
# The same code in linked list for get method can be used here also. But to reduce the time complexity, we write the code bit differently
    def get_value(self, index):
        if  index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2: # if the index is in 1st half
            for _ in range(index): # if index is 0, for loop won't execute anything
                temp = temp.next
        else :                     # if the index is in 2nd half
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp
    
My_Linked_list = DoublyLinkedlist(1)
My_Linked_list.append_to_list(2)
My_Linked_list.append_to_list(3)
print(My_Linked_list.get_value(1))

# Output
"""

<__main__.Node object at 0x0000027139501450>

"""

# 7.SET VALUE METHOD
# Changes or sets an element at a particular index in Doubly linked list
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
class DoublyLinkedlist:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def print_list(self):
        if self.length == 0:
            return None
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def append_to_list(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True  
    def get_value(self, index):
        if  index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2: 
            for _ in range(index): 
                temp = temp.next
        else :
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp
    def set_value(self, value, index):
        temp = self.get_value(index)
        if temp is not None:
            temp.value = value
            return True
        return False
    
My_Linked_list = DoublyLinkedlist(1)
My_Linked_list.append_to_list(2)
My_Linked_list.print_list()
My_Linked_list.set_value(4,1)
My_Linked_list.print_list()

# Output
""""

1
2
1
4

"""

# 8.INSERT METHOD
# Inserts an element at a particular index in Doubly linked list
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
class DoublyLinkedlist:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def print_list(self):
        if self.length == 0:
            return None
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def append_to_list(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True  
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True  
    def get_value(self, index):
        if  index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2: 
            for _ in range(index): 
                temp = temp.next
        else :
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp
    def insert(self, value, index):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append_to_list(value)
        new_node = Node(value)
        before = self.get_value(index-1)
        after  = before.next
        new_node.next = after
        after.prev = new_node
        before.next = new_node
        new_node.prev = before
        self.length += 1
        return True

My_Linked_list = DoublyLinkedlist(1)
My_Linked_list.append_to_list(2)
My_Linked_list.print_list()
My_Linked_list.insert(7,1)
My_Linked_list.print_list()

# Output
"""

1
2
1
7
2

"""

# 9.REMOVE METHOD
# Removes an element from the Doubly linked list
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
class DoublyLinkedlist:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def print_list(self):
        if self.length == 0:
            return None
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def append_to_list(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True  
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:   
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next 
            self.head.prev = None
            temp.next = None
        self.length -= 1 
        return temp
    def pop(self):
        if self.length == 0: 
            return None
        temp = self.tail  
        if self.length == 1:   
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev 
            temp.prev = None
        self.length -= 1 
        return temp
    def get_value(self, index):
        if  index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2: 
            for _ in range(index): 
                temp = temp.next
        else :
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        before = self.get_value(index-1)
        temp = self.get_value(index)    
        after = before.next  
        before.next = after
        after.prev = before
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp
    
My_Linked_list = DoublyLinkedlist(1)
My_Linked_list.append_to_list(2)
My_Linked_list.append_to_list(3)
My_Linked_list.print_list()
print(My_Linked_list.remove(1))
My_Linked_list.print_list()

# Output
"""

1
2
3
<__main__.Node object at 0x0000012BECCB04D0>
1
2

"""

