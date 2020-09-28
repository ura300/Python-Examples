x = [10, 2, 5, 7]
x.sort()
print(x)
[2, 5, 7, 10]
fib = lambda x : 1 if x <= 2 else fib(x - 1) + fib(x - 2)
fib(31)
