def gcd (a, b ):
    if(a == 0 or b == 0):
        return (a+b)
    return gcd(b, a%b)
a= gcd(8,10)
print(a)