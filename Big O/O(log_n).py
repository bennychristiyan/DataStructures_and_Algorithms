# say, a list has n items. Instead of iterating through each item in the list, we can cut the list in half until one item is left
# if the list has 8 items, it will only take 3 operations to find an item in that list (2^3 = 8 --> 3 = log8 (base 2))
# it is great to use to the program with large n value
# it basically says what power of 2 is equal to n
# line for O(log_n) is very flat (not as flat as O(1)) going along x-axis (n) or bottom of the graph and very efficient than O(n) and O(n^2)
# Sorting algorithm --> O(nlog_n)
# O(log_n) is also called divide and conquer