def factorial(n):
    if n < 0:       # so sánh giá trị n với 0 
        return -1  # nếu n< 0 trả giá trị về -1
    elif n == 0:   # ngược lại của if so sánh giá trị n với 0
        return 1    # nếu n = 0 thì trả giá trị về 1
    else:          # ngược lại if 
        return n * factorial(n-1)  # trả giá trị về n* factorial(n-1)
a= factorial(5)
print(a)