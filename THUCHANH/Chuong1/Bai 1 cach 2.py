# cach 2 không dùng đệ quy
def fibonaci(n):
    f0 = 0 
    f1 = 1
    fn = 1
    if ( n < 0):
        print(" nhập lại số nguyên n")
    elif(n == 0 or n ==1):
        return n
    else:
        for i in range (2, n):
            f0 = f1
            f1 = fn
            fn = f0 + f1
        return fn
a = fibonaci(6)
print(a)
    