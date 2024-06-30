#In dynamic programming, we have two different ways of solving problems. One is called top down and the other one is called bottom up.

#Fibonacci sequence done recursively is top down. Top down means that the first thing that we try to solve is the highest number. That's the 
#first thing that goes on the call stack. Then we work our way down to the bottom. When we did this recursively, we started on the right side of 
#the list and work the other direction or top down. That's what we have done in fibonacci sequence and memoization concepts

#Fibonacci sequence done iteratively is bottom up. Bottom up means that the first thing that we try to solve is the lowest number. That's the 
#first thing that goes on the call stack. Then we work our way up to the top. When we do this iteratively, we start on the left side of the list 
#and work the other direction or bottom up.
#The time complexity is O(n-1) (i.e) O(n)
counter = 0

def fib(n):
    fib_list = [0, 1]
    global counter

    for i in range(2, n+1):
        counter += 1
        next_fib = fib_list[i-1] + fib_list[i-2]
        fib_list.append(next_fib)
    
    return fib_list[n]

n1 = 7
n2 = 20 

print("Fib of ", n1 ,"= ", fib(n1))
print("Counter: ", counter)
print("\nFib of ", n2 ,"= ", fib(n2))
print("Counter: ", counter)

#Output
"""

Fib of  7 =  13
Counter:  6

Fib of  20 =  6765
Counter:  19

"""
#In iterative solutions, the computations are typically performed in a single pass using loops. Since the intermediate results are naturally 
#stored in variables or arrays and updated iteratively, there's no need for an additional memoization structure. Each step builds directly on the 
#previous steps, ensuring that all necessary information is available and reused without explicit memoization