def TrungHang(mang):
    rows = len(mang)
    cols = len(mang[0])

    for i in range(rows):
        for j in range(i + 1, rows):
            if mang[i] == mang[j]:
                return True

    return False

# Test
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 2, 3]
]

print("Has identical rows:", TrungHang(matrix))
