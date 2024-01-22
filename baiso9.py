def allFib(n):
    for i in range(n):   
        print(str(i)+":, " + str(fib(i)))  

def fib(n):
    if n <= 0: # so sánh n với 0
        return 0  # nếu n=0 trả giá trị về 0
    elif n == 1:  # so sánh n với 1
        return 1 # nếu n =1 trả giá trị về 1
    return fib(n-1) + fib(n-2)  # trả giá trị về fib(n-1) + fib(n-2)
a = fib(5)
print(a)