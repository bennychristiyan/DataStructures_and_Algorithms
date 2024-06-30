"""Implement the find_kth_from_end function, which takes the LinkedList (ll) and an integer k as input, and returns the k-th node from the end of 
the linked list WITHOUT USING LENGTH.

Given this LinkedList:
1 -> 2 -> 3 -> 4

If k=1 then return the first node from the end (the last node) which contains the value of 4.
If k=2 then return the second node from the end which contains the value of 3, etc.
If the index is out of bounds, the program should return None"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
  

def find_kth_from_end(my_linked_list,k):
    if not my_linked_list.head or k <= 0:
        return None
    slow = my_linked_list.head
    fast = my_linked_list.head
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    return slow
        
        




my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
result = find_kth_from_end(my_linked_list, k)
if result is not None:
    print(result.value) 
else:
    print("None")

#Output
"""

4
    
"""

