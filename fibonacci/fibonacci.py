def fib(n):
    """"Returns the n-th Fibonacic number"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)
