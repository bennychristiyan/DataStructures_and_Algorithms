"""Given an unsorted array of integers, write a function that finds the length of the  longest_consecutive_sequence (i.e., sequence of integers 
in which each element is one greater than the previous element).

Use sets to optimize the runtime of your solution.

Input: An unsorted array of integers, nums.

Output: An integer representing the length of the longest consecutive sequence in nums"""

def longest_consecutive_sequence(nums):
    num_set = set(nums)
    longest_sequence = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_sequence = 1
            while num + 1 in num_set:
                num += 1
                current_sequence += 1
            longest_sequence = max(longest_sequence, current_sequence)

    return longest_sequence

print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )


#Output
"""

    4

"""