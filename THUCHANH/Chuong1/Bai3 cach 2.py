def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
a= gcd(372, 84)
print(a)
