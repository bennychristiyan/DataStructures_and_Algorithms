# n + n = 2n, O(2n) = O(n), O(n) = O(10n) (or) O(100n) etc,. (in a graph)
# The constant before n is not considered, in other words constants are dropped 

def print_items(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)    

print_items(10)

# output
"""

0
1
2
3
4
5
6
7
8
9
0
1
2
3
4
5
6
7
8
9

"""