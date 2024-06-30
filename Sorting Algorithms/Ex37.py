"""Assignment:
Write a selection_sort() method in the LinkedList class that will sort the elements of a linked list in ascending order using the selection sort 
algorithm. The method should update the head and tail pointers of the linked list to reflect the new order of the nodes in the list. You can 
assume that the input linked list will contain only integers. You should not use any additional data structures to sort the linked list.

Input:
The LinkedList object containing a linked list with unsorted elements (self).

Output:
None. The method sorts the linked list in place.

Method Description:
If the length of the linked list is less than 2, the method returns and the list is assumed to be already sorted.
The selection sort algorithm works by repeatedly finding the smallest element in the unsorted part of the list and swapping it with the first 
element in the unsorted part of the list.
The method starts with the entire linked list being the unsorted part of the list.
For each pass through the unsorted part of the list, the method iterates through each element to find the smallest element in the unsorted part 
of the list. Once the smallest element is found, it is swapped with the first element in the unsorted part of the list.
After each pass, the smallest element in the unsorted part of the list will be at the beginning of the unsorted part of the list.
The method continues iterating through the unsorted part of the list until the entire list is sorted.
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

    def selection_sort(self):
        if self.length <= 1:
            return
        start = self.head
        while start is not None:
            min_node = start
            current = start.next
            while current is not None:
                if current.value < min_node.value:
                    min_node = current
                current = current.next
            if min_node != start:
                min_node.value, start.value = start.value, min_node.value
            start = start.next



my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.selection_sort()

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

