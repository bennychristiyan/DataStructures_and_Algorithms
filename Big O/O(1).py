# in other big O's, as n increases, the no. of operations increases
# but in O(1), no matter the value of n, you always have only one operation
# O(1) is also called as constant time, because as n increases, the number of operations remains constant
# line for O(1) is flat going along x-axis (n) or bottom of the graph as the no. of operations remains constant

def add_items(n):
    return n + n 

# Even if we have 2 additions, the no. of operations still remains constant as n increases

def add_items(n):
    return n + n + n
