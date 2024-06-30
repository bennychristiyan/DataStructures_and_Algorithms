#Fibonacci sequence can be executed by using the answers of the previous identical subproblems. Hence, this becomes very efficient
#Fibonacci sequence using memoization concept. The time complexity is O(2n-1) (i.e) O(n)
counter = 0

memo = [None] * 100

def fib(n):
    global counter
    counter += 1
    
    if memo[n] is not None:
        return memo[n]

    if n == 0 or n ==1:
        return n 
    
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

n1 = 7
n2 = 20 

print("Fib of ", n1 ,"= ", fib(n1))
print("Counter: ", counter)
print("\nFib of ", n2 ,"= ", fib(n2))
print("Counter: ", counter)

#Output
"""

Fib of  7 =  13
Counter:  13

Fib of  20 =  6765
Counter:  40

"""