# cach 2 không dùng đệ quy
def fibonaci(n):
    a = 0 
    b = 1
    c = 1
    if ( n < 0):
        print(" nhập lại số nguyên n")
    elif(n == 0 or n ==1):
        return n
    else:
        for i in range (2, n):
            a = b
            b = c
            c = a + b
        return c
a = fibonaci(6)
print(a)
    