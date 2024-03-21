def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def binomial_coefficient(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def print_pascal_triangle(n):
    for line in range(n):
        for i in range(line + 1):
            print(binomial_coefficient(line, i), end=" ")
        print()
a= print_pascal_triangle(5)
print(a)