"""Assignment:
Your task is to implement the bubble_sort method within the LinkedList class. The bubble_sort method should sort the elements of the linked list 
in ascending order based on their values. The sorting should be done in-place, meaning you should not create a new linked list but rather modify 
the existing one.

Requirements:
The bubble_sort method should iterate through the linked list, comparing each pair of adjacent nodes and swapping their values if they are in the 
wrong order. This process should repeat until the entire list is sorted.
The method must handle linked lists of any length, including empty lists and lists with only one element. In cases where the list is empty or 
contains only one element, the method should simply return without making any changes.
You should not use any external libraries or built-in sorting functions to implement the sorting logic.
Optimize the bubble_sort method to stop early if the list becomes sorted before going through all the iterations

Input:
The LinkedList object containing a linked list with unsorted elements (self).

Output:
None. The method sorts the linked list in place.

Method Description:
If the length of the linked list is less than 2, the method returns and the list is assumed to be already sorted.
The bubble sort algorithm works by repeatedly iterating through the unsorted part of the list, comparing adjacent elements and swapping them if 
they are in the wrong order.
The method starts with the entire linked list being the unsorted part of the list.
For each pass through the unsorted part of the list, the method iterates through each pair of adjacent elements and swaps them if they are in the 
wrong order.
After each pass, the largest element in the unsorted part of the list will "bubble up" to the end of the list.
The method continues iterating through the unsorted part of the list until no swaps are made during a pass.
After the linked list is fully sorted, the head and tail pointers of the linked list are updated to reflect the new order of the nodes in the list.

Constraints:
The linked list can contain duplicates.
The method should be implemented in the LinkedList class.
The method should not use any additional data structures to sort the linked list."""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
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
            self.tail = new_node
        self.length += 1

    def bubble_sort(self):
        if self.length <= 1:
            return
        else:
            for i in range(self.length-1, 0, -1):
                temp = self.head
                for j in range(i):
                    if temp.value > temp.next.value:
                        temp.value, temp.next.value = temp.next.value, temp.value
                    temp = temp.next
                



my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.bubble_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()


#Output
"""

    Linked List Before Sort:
    4
    2
    6
    5
    1
    3

    Sorted Linked List:
    1
    2
    3
    4
    5
    6

"""

