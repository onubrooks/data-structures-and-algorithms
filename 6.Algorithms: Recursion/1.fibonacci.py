# Given a number N return the index value of the Fibonacci sequence, where the sequence is:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...
# the pattern of the sequence is that each value is the sum of the 2 previous values, that means that for N=5 → 2+3

# For example: fibonacciRecursive(6) should return 8

def fibonacci_iterative(n):
    arr = [0,1]
    for i in range(2, n+1):
        arr.append(arr[i-1]+arr[i-2])
    return arr[n]


print(fibonacci_iterative(0))
print(fibonacci_iterative(1))
print(fibonacci_iterative(2))
print(fibonacci_iterative(3))
print(fibonacci_iterative(4))
print(fibonacci_iterative(5))
  
def fibonacci_recursive(n):
    if n < 2:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

print(fibonacci_recursive(0))
print(fibonacci_recursive(1))
print(fibonacci_recursive(2))
print(fibonacci_recursive(3))
print(fibonacci_recursive(4))
print(fibonacci_recursive(5))