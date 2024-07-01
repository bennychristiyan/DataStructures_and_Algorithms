"""Write a Python function that takes a list of integers as input and returns a tuple containing the maximum and minimum values in the list.
The function should have the following signature:

def find_max_min(myList):

Where myList is the list of integers to search for the maximum and minimum values
The function should traverse the list and keep track of the current maximum and minimum values. It should then return these values as a tuple, 
with the maximum value as the first element and the minimum value as the second element.
For example, if the input list is [5, 3, 8, 1, 6, 9], the function should return (9, 1) since 9 is the maximum value and 1 is the minimum value."""

def find_max_min(my_list):
    mini = my_list[0]
    maxi = my_list[0]
    for i in range(1, len(my_list)):
        if mini > my_list[i]:
            mini = my_list[i]
        elif maxi < my_list[i]:
            maxi = my_list[i]
        
    return maxi, mini


print( find_max_min([5, 3, 8, 1, 6, 9]) )

#Output
"""

    (9, 1)
    
"""