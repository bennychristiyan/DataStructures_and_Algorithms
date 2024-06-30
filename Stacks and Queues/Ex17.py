"""The sort_stack function takes a single argument, a Stack object.  The function should sort the elements in the stack in ascending order (the 
lowest value will be at the top of the stack) using only one additional stack. 

The function should use the pop, push, peek, and is_empty methods of the Stack object.
Note: This is a new function, not a method within the Stack class. So, your indent should be all the way to the LEFT."""

class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()
            
def sort_stack(stack):
    aux_stack = Stack()

    while not stack.is_empty():
        current_element = stack.pop()

        while not aux_stack.is_empty() and aux_stack.peek() > current_element:
            stack.push(aux_stack.pop())

        aux_stack.push(current_element)

    while not aux_stack.is_empty():
        stack.push(aux_stack.pop())





my_stack = Stack()
my_stack.push(3)
my_stack.push(1)
my_stack.push(5)
my_stack.push(4)
my_stack.push(2)

print("Stack before sort_stack():")
my_stack.print_stack()

sort_stack(my_stack)

print("\nStack after sort_stack:")
my_stack.print_stack()


#Output
"""

    Stack before sort_stack():
    2
    4
    5
    1
    3

    Stack after sort_stack:
    1
    2
    3
    4
    5

"""