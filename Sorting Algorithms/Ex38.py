"""Assignment:
Write an insertion_sort() method in the LinkedList class that will sort the elements of a linked list in ascending order using the insertion sort 
algorithm.
The method should update the head and tail pointers of the linked list to reflect the new order of the nodes in the list.
You can assume that the input linked list will contain only integers. You should not use any additional data structures to sort the linked list.

Input:
The LinkedList object containing a linked list with unsorted elements (self).

Output:
None. The method sorts the linked list in place.

Method Description:
If the length of the linked list is less than 2, the method returns and the list is assumed to be already sorted.
The first element of the linked list is treated as the sorted part of the list, and the second element is treated as the unsorted part of the list.
The first element of the sorted part of the list is then disconnected from the rest of the list, creating a new linked list with only one element.
The method then iterates through each remaining node in the unsorted part of the list.
For each node in the unsorted part of the list, the method determines its correct position in the sorted part of the list by comparing its value 
with the values of the other nodes in the sorted part of the list.
Once the correct position has been found, the node is inserted into the sorted part of the list at the appropriate position.
After all the nodes in the unsorted part of the list have been inserted into the sorted part of the list, the head and tail pointers of the linked
list are updated to reflect the new order of the nodes in the list.

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

    def insertion_sort(self):
        if self.length <= 1:
            return
        sorted_tail = self.head
        current = self.head.next
        sorted_tail.next = None

        while current is not None:
            next_node = current.next

            if current.value < self.head.value:
                current.next = self.head
                self.head = current
            else:
                search = self.head
                while search.next is not None and search.next.value < current.value:
                    search = search.next
                current.next = search.next
                search.next = current

            current = next_node

        temp = self.head
        while temp.next is not None:
            temp = temp.next
        self.tail = temp
        

my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.insertion_sort()

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

