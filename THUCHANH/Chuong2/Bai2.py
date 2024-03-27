def TamGiacTren(matrix):
    n = len(matrix)
    
    # Kiểm tra từng phần tử nằm dưới đường chéo chính
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != 0:  # Nếu phần tử không bằng 0, không phải ma trận tam giác trên
                return False
    return True  # Nếu không có phần tử nào khác 0 nằm dưới đường chéo chính, là ma trận tam giác trên

# Ví dụ sử dụng:
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

print(TamGiacTren(matrix1))  # Output: True
print(TamGiacTren(matrix2))  # Output: False
