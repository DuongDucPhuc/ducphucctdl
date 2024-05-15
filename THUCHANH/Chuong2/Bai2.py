def TamGiacTren(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != 0: 
                return False
    return True  
matrix1 = [
    [1, 2, 3],
    [0, 4, 5],
    [0, 0, 6]
]

matrix2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(TamGiacTren(matrix1))  
print(TamGiacTren(matrix2)) 
