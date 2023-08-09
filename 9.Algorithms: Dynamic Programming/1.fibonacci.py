def fibonacci(n):
    global calculations
    calculations += 1
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

calculations = 0
print(fibonacci(15)) # O(2^n) time
print(f'calc 15: {calculations}')

def fibonacci_better():
    cache = {}
    def inner_fib(n):
        global calculations2
        calculations2 += 1
        if n in cache:
            return cache[n]
        else:
            if n < 2:
                return n
            else:
                cache[n] = inner_fib(n-1) + inner_fib(n-2)
                return cache[n]
    return inner_fib

fib_dynamic = fibonacci_better()

calculations2 = 0
print(fib_dynamic(15)) # O(n) time
print(f'calc 15: {calculations2}')

def fibonacci_bottom_up(n):
    fibs = [0,1]
    for i in range(2, n+1):
        fibs.append(fibs[i-1] + fibs[i-2])
    return fibs.pop()

print(fibonacci_bottom_up(15))