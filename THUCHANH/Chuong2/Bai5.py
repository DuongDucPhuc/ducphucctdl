class acongb:
    def __init__(self, mang):
        self.mang = mang

    def mangthanhsonguyen(self, mang):
        return int(''.join(map(str, mang)))
    
    def songuyenthanhmang(self, num):
        return list(map(int, str(num)))
    
    def Cong(self, b):
        songuyena = self.mangthanhsonguyen(self.mang)
        songuyenb = self.mangthanhsonguyen(b.mang)
        
        result = songuyena + songuyenb
        
        return self.songuyenthanhmang(result)

a = acongb([1, 2, 3])
b = acongb([1, 0, 1])
c = a.Cong(b)
print(c)