"""Implement the partition_list member function for the LinkedList class, which partitions the list such that all nodes with values less than x come before nodes with values greater than or equal to x.
Note:  This linked list class does NOT have a tail which will make this method easier to implement.
The original relative order of the nodes should be preserved.

Details:
The function partition_list takes an integer x as a parameter and modifies the current linked list in place according to the specified criteria. 
If the linked list is empty (i.e., head is null), the function should return immediately without making any changes.

Example:
Input:
Linked List: 3 -> 8 -> 5 -> 10 -> 2 -> 1 x: 5
Process:
Values less than 5: 3, 2, 1
Values greater than or equal to 5: 8, 5, 10
Output:
Linked List: 3 -> 2 -> 1 -> 8 -> 5 -> 10"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1 
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def partition_list(self, x):
        if not self.head:
            return

        less_than_x_head = None
        less_than_x_tail = None
        greater_equal_x_head = None
        greater_equal_x_tail = None

        current_node = self.head

        while current_node:
            if current_node.value < x:
                if less_than_x_head is None:
                    less_than_x_head = current_node
                    less_than_x_tail = current_node
                else:
                    less_than_x_tail.next = current_node
                    less_than_x_tail = current_node
            else:
                if greater_equal_x_head is None:
                    greater_equal_x_head = current_node
                    greater_equal_x_tail = current_node
                else:
                    greater_equal_x_tail.next = current_node
                    greater_equal_x_tail = current_node

            current_node = current_node.next

        # Connect the two new linked lists
        if less_than_x_head:
            self.head = less_than_x_head
            less_than_x_tail.next = greater_equal_x_head
        else:
            self.head = greater_equal_x_head

        # Make sure to set the tail of the greater/equal to x list to None
        if greater_equal_x_tail:
            greater_equal_x_tail.next = None

    
    

ll = LinkedList(3)
ll.append(5)
ll.append(8)
ll.append(10)
ll.append(2)
ll.append(1)

print("LL before partition_list:")
ll.print_list() 

ll.partition_list(5)

print("LL after partition_list:")
ll.print_list()

#Output
"""

    LL before partition_list:
    3
    5
    8
    10
    2
    1
    LL after partition_list:
    3
    2
    1
    5
    8
    10
    
"""




