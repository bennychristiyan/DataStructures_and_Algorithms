# consider a list l = [11,3,23,7]

# adding a number 17 (l.append(17)) (l = [11,3,23,7,17]) 
# or removing the number 17 (l.pop()) (l = [11,3,23,7]) at the end of the list does not reindex the list, which is O(1)
# in a list if you directly access the value at a specific index without iterating, it is O(1)

# removing 11 (l.pop(0)) (l = [3,23,7]) 
# or adding 11 (l.insert(0,11)) to its original position reindex the whole list, which is O(n)
# in a list if you iterate one by one through a loop to find a value, it is O(n)
# if a number is added or removed in/from the middle of the list, it is still O(n) 
# It is not O(1/2n) as big O measures worst cases not average cases and the constants are dropped
