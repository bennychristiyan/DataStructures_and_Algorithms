"""You are given two lists of integers, arr1 and arr2, and a target integer value, target. Your task is to find all pairs of numbers (one from 
arr1 and one from arr2) whose sum equals target.

Write a function called find_pairs that takes in three arguments: arr1, arr2, and target, and returns a list of all such pairs.  Assume that each 
array does not contain duplicate values.

The tests for this exercise assume that arr1 is the list being converted to a set.

Input
Your function should take in the following inputs:
arr1: a list of integers
arr2: a list of integers
target: an integer

Output
Your function should return a list of tuples, where each tuple contains two integers from arr1 and arr2 that add up to target"""

def find_pairs(arr1, arr2, target):
    pairs = []
    # Create a set from arr2 for fast lookup
    set_arr2 = set(arr2)
    # Iterate through arr1
    for num1 in arr1:
        # Calculate the complement needed to reach the target
        complement = target - num1
        # Check if the complement exists in arr2
        if complement in set_arr2:
            # If it does, add the pair to the result list
            pairs.append((num1, complement))
    return pairs
                




arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)


#Output
"""

    [(5, 2), (3, 4), (1, 6)]

"""