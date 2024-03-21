def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
def neper(n):
    if n < 0:
        print("nhap lai so nguyen n")
    else:
        tong = 0
        for k in range(n+1):
            ak = 1/ factorial(k)
            tong = ak + 1
        return tong
a = neper(0)
print(a)