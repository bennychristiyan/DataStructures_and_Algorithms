"""You are given a singly linked list that contains integer values, where some of these values may be duplicated.
Note: this linked list class does NOT have a tail which will make this method easier to implement.
Your task is to implement a method called remove_duplicates() within the LinkedList class that removes all duplicate values from the list.
Your method should not create a new list, but rather modify the existing list in-place, preserving the relative order of the nodes.

Example:
Input:
LinkedList: 1 -> 2 -> 3 -> 1 -> 4 -> 2 -> 5
Output:
LinkedList: 1 -> 2 -> 3 -> 4 -> 5"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next  
            
    def print_all(self):
        if self.length == 0:
            print("Head: None")
        else:
            print("Head: ", self.head.value)
        print("Length: ", self.length)
        print("\nLinked List:")
        if self.length == 0:
            print("empty")
        else:
            self.print_list()

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1


    def remove_duplicates(self):
        if self.length <= 1:
            return
        current = self.head
        while current is not None:
            runner = current
            while runner.next is not None:
                if runner.next.value == current.value:
                    runner.next = runner.next.next
                    self.length -= 1
                else:
                    runner = runner.next
            current = current.next
                
    



my_linked_list = LinkedList(1)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(3)
my_linked_list.append(2)
my_linked_list.append(4)
my_linked_list.remove_duplicates()

my_linked_list.print_all()



#Output
"""

    Head:  1
    Length:  4
    Linked List:
    1
    2
    3
    4
    
"""
