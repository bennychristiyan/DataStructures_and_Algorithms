#The node class can be used for various methods such as append, prepend, insert without writing a code to create a node everytime
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

My_Linked_list = Linkedlist(4)

print(My_Linked_list.head.value)
print(My_Linked_list.head.next)

# Output
"""

4
None

"""