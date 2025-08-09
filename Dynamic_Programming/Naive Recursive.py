def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))

# The naive recursive approach to computing the $ n $-th Fibonacci number uses the basic definition of the Fibonacci sequence: each number is the sum of the two preceding ones, starting with $ F(0) = 0 $ and $ F(1) = 1 $. So, $ F(n) = F(n-1) + F(n-2) $.