class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

# constructor
class Linkedlist:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

# 1.PRINT LINKED LIST
# It prints all the alements in the entire linked list
    def print_list(self):
        if self.length == 0:
            return None
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

# 2.APPEND TO A LINKED LIST
# It adds an element to the end of the linked list
    def append_to_list(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True  # optional
    
# 3.POP METHOD
# Removes the last element from a linked list
    def pop(self):
        if self.length == 0: # if the list is empty, it returns None
            return None
        temp = self.head  # if the list has 2 or more elements, it removes the last element and the tail points to the second to last element
        pre = self.head
        while(temp.next is not None):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1 
        if self.length == 0:  # if the list has one element, the head and tail points to None after pop 
            self.head = None
            self.tail = None
        return temp



My_Linked_list = Linkedlist(1)
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
<__main__.Node object at 0x00000241914D0F50>
<__main__.Node object at 0x00000241914D0F90>
None
None

"""

# 4.PREPEND METHOD
# It adds an element to the beginning of the linked list
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Linkedlist:
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
            self.head = new_node
        self.length += 1
        return True  # optional

My_Linked_list = Linkedlist(1)
My_Linked_list.prepend(3)
My_Linked_list.print_list()

# Output
"""

3
1

"""

# 5.POP FIRST METHOD
# Removes the first element from a linked list
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Linkedlist:
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
            self.tail = new_node
        self.length += 1
        return True 
    def pop_first(self):
            if self.length == 0: # if the list is empty, it returns None
                return None
            temp = self.head  # if the list has 2 or more elements, it removes the first element and the head points to the second element
            self.head = self.head.next
            temp.next = None
            self.length -= 1 
            if self.length == 0:  # if the list has one element, the head and tail points to None after pop first 
                self.tail = None  # self.head is already None due to self.head.next
            return temp
    
My_Linked_list = Linkedlist(1)
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
<__main__.Node object at 0x00000241914D0B90>
<__main__.Node object at 0x00000241914D0E10>
None
None

"""
    
# 6.GET VALUE METHOD
# Gets a element in the linked list using index
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Linkedlist:
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
            self.tail = new_node
        self.length += 1
        return True  
    def get_value(self, index):
        if  index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index): # if index is 0, for loop won't execute anything
            temp = temp.next
        return temp
    
My_Linked_list = Linkedlist(1)
My_Linked_list.append_to_list(2)
My_Linked_list.append_to_list(3)
print(My_Linked_list.get_value(1))

# Output
"""

<__main__.Node object at 0x0000029328C60D50>

"""
    
# 7.SET VALUE METHOD
# Changes or sets an element at a particular index in linked list
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Linkedlist:
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
            self.tail = new_node
        self.length += 1
        return True  
    def get_value(self, index):
        if  index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    def set_value(self, value, index):
        temp = self.get_value(index)
        if temp is not None:
            temp.value = value
            return True
        return False
    
My_Linked_list = Linkedlist(1)
My_Linked_list.append_to_list(2)
My_Linked_list.print_list()
My_Linked_list.set_value(4,1)
My_Linked_list.print_list()

# Output
"""

1
2
1
4

"""
    
# 8.INSERT METHOD
# Inserts an element at a particular index in linked list
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Linkedlist:
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
            self.head = new_node
        self.length += 1
        return True
    def get_value(self, index):
        if  index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index): 
            temp = temp.next
        return temp
    def insert(self, value, index):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append_to_list(value)
        new_node = Node(value)
        temp = self.get_value(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

My_Linked_list = Linkedlist(1)
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
# Removes an element from the linked list
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Linkedlist:
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
            self.tail = new_node
        self.length += 1
        return True 
    def pop_first(self):
            if self.length == 0:
                return None
            temp = self.head  
            self.head = self.head.next
            temp.next = None
            self.length -= 1 
            if self.length == 0:  
                self.tail = None  
            return temp
    def pop(self):
        if self.length == 0: 
            return None
        temp = self.head  
        pre = self.head
        while(temp.next is not None):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1 
        if self.length == 0:  
            self.head = None
            self.tail = None
        return temp
    def get_value(self, index):
        if  index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index): 
            temp = temp.next
        return temp
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get_value(index-1)
        temp = self.get_value(index)      
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
My_Linked_list = Linkedlist(1)
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
<__main__.Node object at 0x0000017051C707D0>
1
3

"""
    
# 10.REVERSE METHOD
# Reverse the entire linked list
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Linkedlist:
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
            self.tail = new_node
        self.length += 1
        return True 
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


My_Linked_list = Linkedlist(1)
My_Linked_list.append_to_list(2)
My_Linked_list.append_to_list(3)
My_Linked_list.print_list()
My_Linked_list.reverse()
My_Linked_list.print_list()

# Output
"""

1
2
3
3
2
1

"""

    

