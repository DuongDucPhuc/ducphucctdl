class anhanb:
    def __init__(self, a):
        self.a = a

    def Nhan(self, b):
        songuyena = ''.join(str(x) for x in self.a)
        songuyenb = ''.join(str(x) for x in b)
        result = int(songuyena) * int(songuyenb)

        # Kiểm tra xem kết quả có vượt quá giới hạn của số nguyên 32 bit không
        if result > 2**31 - 1 or result < -2**31:
            return [-1]
        else:
            return result

a = anhanb([1, 2, 3])
print(a.Nhan([4, 5, 6])) 