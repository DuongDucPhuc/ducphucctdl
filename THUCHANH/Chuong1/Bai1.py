def fibonacci(x):
    if x ==0 or x == 1:
        return x
    return fibonacci(x-1) + fibonacci (x-2)
a = fibonacci(6)
print(a)