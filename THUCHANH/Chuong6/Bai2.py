def Hieu(a, b):
    set_b = set(b)
    c=[]
    for num in a:
        if num not in set_b and num not in c:
            c.append(num)
    c.sort()
    return c
a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]
c = Hieu(a, b )
print(c)