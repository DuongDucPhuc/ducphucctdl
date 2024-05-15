def Tam_Giac_Duoi(mang):
    n = len(mang) 
    
    for i in range(n):
        for j in range(i):
            if mang[i][j] != 0:
                return False
    
    return True

mang1 = [[1, 0, 0], [4, 5, 0], [6, 7, 8]]
mang2 = [[1, 2, 0], [0, 5, 6], [0, 0, 8]]

print(Tam_Giac_Duoi(mang1)) 
print(Tam_Giac_Duoi(mang2))  