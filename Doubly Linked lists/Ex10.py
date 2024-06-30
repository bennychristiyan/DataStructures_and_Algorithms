#Write a method to determine whether a given doubly linked list reads the same forwards and backwards.
#For example, if the list contains the values [1, 2, 3, 2, 1], then the method should return True, since the list is a palindrome.
#If the list contains the values [1, 2, 3, 4, 5], then the method should return False, since the list is not a palindrome.
#Method name: is_palindrome

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def is_palindrome(self):
        if not self.head:
            return True
    
        forward_values = []
        backward_values = []
        
        current_node = self.head
        
        # Traverse the list forwards
        while current_node:
            forward_values.append(current_node.value)
            current_node = current_node.next
        
        current_node = self.tail
        
        # Traverse the list backwards
        while current_node:
            backward_values.append(current_node.value)
            current_node = current_node.prev
        
        # Check if the values read the same forwards and backwards
        return forward_values == backward_values




my_dll_1 = DoublyLinkedList(1)
my_dll_1.append(2)
my_dll_1.append(3)
my_dll_1.append(2)
my_dll_1.append(1)

print('my_dll_1 is_palindrome:')
print( my_dll_1.is_palindrome() )


my_dll_2 = DoublyLinkedList(1)
my_dll_2.append(2)
my_dll_2.append(3)

print('\nmy_dll_2 is_palindrome:')
print( my_dll_2.is_palindrome() )


#Output
"""

    my_dll_1 is_palindrome:
    True

    my_dll_2 is_palindrome:
    False

"""

