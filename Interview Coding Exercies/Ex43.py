"""Given a sorted list of integers, rearrange the list in-place such that all unique elements appear at the beginning of the list.
Your function should return the new length of the list containing only unique elements. Note that you should not create a new list or use any 
additional data structures to solve this problem. The original list should be modified in-place.

Constraints:
    The input list is sorted in non-decreasing order.
    The input list may contain duplicates.
    The function should have a time complexity of O(n), where n is the length of the input list.
    The function should have a space complexity of O(1), i.e., it should not use any additional data structures or create new lists (this also means you cannot use a set like we did earlier in the course).

Example:
Input: nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4] Function call: new_length = remove_duplicates(nums) Output: new_length = 5 Modified list: 
nums = [0, 1, 2, 3, 4, 2, 2, 3, 3, 4] (first 5 elements are unique)

Explanation: The function modifies the original list nums in-place, moving unique elements to the beginning of the list, followed by duplicate 
elements. The new length returned by the function is 5, indicating that there are 5 unique elements in the list. The first 5 elements of the 
modified list nums are the unique elements [0, 1, 2, 3, 4]"""

def remove_duplicates(nums):
    if not nums:
        return 0

    unique_index = 1
    
    for i in range(1, len(nums)):
        if nums[i-1] != nums[i]:
            nums[unique_index] = nums[i]
            unique_index += 1

    return unique_index 
            
# Test case 1: Empty list
test1 = []
print(f"Test 1 Before: {test1}")
result1 = remove_duplicates(test1)
print(f"Test 1 After: {test1[:result1]}")
print(f"New Length: {result1}")
print("------")

# Test case 2: List with all duplicates
test2 = [1, 1, 1, 1, 1]
print(f"Test 2 Before: {test2}")
result2 = remove_duplicates(test2)
print(f"Test 2 After: {test2[:result2]}")
print(f"New Length: {result2}")
print("------")

# Test case 3: List with no duplicates
test3 = [1, 2, 3, 4, 5]
print(f"Test 3 Before: {test3}")
result3 = remove_duplicates(test3)
print(f"Test 3 After: {test3[:result3]}")
print(f"New Length: {result3}")
print("------")

# Test case 4: List with some duplicates
test4 = [1, 1, 2, 2, 3, 4, 5, 5]
print(f"Test 4 Before: {test4}")
result4 = remove_duplicates(test4)
print(f"Test 4 After: {test4[:result4]}")
print(f"New Length: {result4}")
print("------")


#Output
"""

Test 1 Before: []
Test 1 After: []
New Length: 0
------
Test 2 Before: [1, 1, 1, 1, 1]
Test 2 After: [1]
New Length: 1
------
Test 3 Before: [1, 2, 3, 4, 5]
Test 3 After: [1, 2, 3, 4, 5]
New Length: 5
------
Test 4 Before: [1, 1, 2, 2, 3, 4, 5, 5]
Test 4 After: [1, 2, 3, 4, 5]
New Length: 5
------

"""