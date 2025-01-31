# Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.

def fibonacci(n):
    x = 0
    y = 1
    next = y

    for i in range(1, n+1):
        print(x)
        x, y = y, next
        next = x + y

fibonacci(100)



        