class MaTran:
    def __init__(self, mang):
        self.mang = mang

    def NhomHang(self):
        n = len(self.mang)
        da_kiem_tra = [False] * n
        nhom_hang = []
        
        for i in range(n):
            if not da_kiem_tra[i]:
                nhom = [i]
                for j in range(i + 1, n):
                    if not da_kiem_tra[j] and self.mang[i] == self.mang[j]:
                        nhom.append(j)
                        da_kiem_tra[j] = True
                nhom_hang.append(nhom)
                da_kiem_tra[i] = True

        for nhom in nhom_hang:
            print("Nhóm hàng giống nhau:", nhom)

mang = [
    [1, 2, 3],
    [4, 5, 6],
    [1, 2, 3],
    [7, 8, 9],
    [4, 5, 6]
]

ma_tran = MaTran(mang)
ma_tran.NhomHang()
