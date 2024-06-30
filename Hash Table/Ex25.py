"""Given an array of integers nums and a target integer target, write a Python function called subarray_sum that finds the indices of a contiguous
subarray in nums that add up to the target sum using a hash table (dictionary).

Your function should take two arguments:
    nums: a list of integers representing the input array
    target: an integer representing the target sum

Your function should return a list of two integers representing the starting and ending indices of the subarray that adds up to the target sum. 
If there is no such subarray, your function should return an empty list"""

def subarray_sum(nums, target):
    num_dict = {}
    current_sum = 0
    for index, num in enumerate(nums):
        current_sum += num
        if current_sum == target:
            return [0, index]
        if (current_sum - target) in num_dict:
            return [num_dict[current_sum - target] + 1, index]
        num_dict[current_sum] = index
    return []

nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )

nums = []
target = 0
print ( subarray_sum(nums, target) )


#Output
"""

    [1, 3]
    [0, 3]
    [1, 1]
    []

"""
