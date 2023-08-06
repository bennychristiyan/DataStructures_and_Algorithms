# O(n^2) + O(n) = O(n^2 + n) = O(n^2) (in a graph)
# when the value of n is very large n^2 becomes a very large number than n
# Hence, n^2 is called dominant term and n is called non-dominant term
# And since the non-dominants become insignificant when the value of n is large, they are dropped

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)  

    for k in range(n):
        print(k) 

print_items(10)

# output
"""

0 0
0 1
0 2
0 3
0 4
0 5
0 6
0 7
0 8
0 9
1 0
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
2 0
2 1
2 2
2 3
2 4
2 5
2 6
2 7
2 8
2 9
3 0
3 1
3 2
3 3
3 4
3 5
3 6
3 7
3 8
3 9
4 0
4 1
4 2
4 3
4 4
4 5
4 6
4 7
4 8
4 9
5 0
5 1
5 2
5 3
5 4
5 5
5 6
5 7
5 8
5 9
6 0
6 1
6 2
6 3
6 4
6 5
6 6
6 7
6 8
6 9
7 0
7 1
7 2
7 3
7 4
7 5
7 6
7 7
7 8
7 9
8 0
8 1
8 2
8 3
8 4
8 5
8 6
8 7
8 8
8 9
9 0
9 1
9 2
9 3
9 4
9 5
9 6
9 7
9 8
9 9
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