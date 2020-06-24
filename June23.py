# June 23
# Given an integer n, write a function to compute the nth Fibonacci number
# Problem source: https://www.byte-by-byte.com/fibonacci/

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(1))
print(fibonacci(5))
print(fibonacci(10))
print(fibonacci(11))
print(fibonacci(12))
