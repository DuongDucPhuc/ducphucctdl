def Duynhat(a):
    a.sort()
    b = []
    for num in a:
        if num not in b:
            b.append(num)
    return b
a=[1, 5, 3, 7, 5, 9, 7]
b=Duynhat(a)
print(b)