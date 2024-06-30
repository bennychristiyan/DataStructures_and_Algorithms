#Fibonacci sequence has overlapping subproblems(functions). Hence, it is very inefficient to execute the same function again and again. 
#Fibonacci sequence without using memoization concept. The time complexity would be O(2^n)
counter = 0

def fib(n):
    global counter
    counter += 1

    if n == 0 or n ==1:
        return n
    
    return fib(n-1) + fib(n-2)

n1 = 7
n2 = 20 

print("Fib of ", n1 ,"= ", fib(n1))
print("Counter: ", counter)
print("\nFib of ", n2 ,"= ", fib(n2))
print("Counter: ", counter)

#Output
"""

Fib of  7 =  13
Counter:  41

Fib of  20 =  6765
Counter:  21932

"""




