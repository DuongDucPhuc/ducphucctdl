def powersOf2(n):
    if n < 1:   # so sánh n với 1
        return 0  # nếu n<1 thì trả giá trị về 0
    elif n == 1:  # so sánh n với 1
        print(1)  # nếu bằng 1 thì in 1
        return 1  # trả giá trị về 1
    else:
        prev = powersOf2(int(n/2))  # gán hàm n/2 với prev
        curr = prev*2    # gán giá trị curr = prev *2
        print(curr)        # in ra giá trị curr
        return curr        # trả về giá trị curr
a = powersOf2(5)
print(a)