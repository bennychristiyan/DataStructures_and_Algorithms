"""find_duplicates()
Problem: Given an array of integers nums, find all the duplicates in the array using a hash table (dictionary).
Input:
A list of integers nums.
Output:
A list of integers representing the numbers in the input array nums that appear more than once. If no duplicates are found in the input array, 
return an empty list []"""

def find_duplicates(nums):
    num_count = {}
    duplicates = []
    
    for num in nums:
        if num in num_count:
            num_count[num] += 1 
        else:
            num_count[num] = 1
            
    for num, count in num_count.items():
        if count > 1:
            duplicates.append(num)
            
    return duplicates
    
            
            




print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )


#Output
"""

    []
    [1, 2]
    [1]
    [3, 4]
    [1, 2, 3]
    [1, 2, 3]
    []

"""

