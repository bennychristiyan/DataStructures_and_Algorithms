# O(a) + O(b) = O(a + b)

def Print_items(a,b):
    for i in range(a):
        print(i)

    for j in range(b):
        print(j) 

# O(a) * O(b) = O(a * b)        

def print_items(a,b):
    for i in range(a):
        for j in range(b):
            print(i,j)

Print_items(10, 5)
print_items(10, 5)

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
0 0
0 1
0 2
0 3
0 4
1 0
1 1
1 2
1 3
1 4
2 0
2 1
2 2
2 3
2 4
3 0
3 1
3 2
3 3
3 4
4 0
4 1
4 2
4 3
4 4
5 0
5 1
5 2
5 3
5 4
6 0
6 1
6 2
6 3
6 4
7 0
7 1
7 2
7 3
7 4
8 0
8 1
8 2
8 3
8 4
9 0
9 1
9 2
9 3
9 4

"""
