def Giao(a, b):
    set_a = set(a)
    set_b = set(b)
    c=[]
    for num in set_a:
        if num in set_b:
            c.append(num)
    return c
a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]
c = Giao(a, b)
print(c)
