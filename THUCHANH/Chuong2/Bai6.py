class atrub:
    def __init__(self, mang):
        self.mang = mang

    def mang_to_int(self, mang):
        return int(''.join(map(str, mang)))
    
    def int_to_mang(self, num):
        return list(map(int, str(num)))
    
    def Tru(self, b):
        a_int = self.mang_to_int(self.mang)
        b_int = self.mang_to_int(b.mang)
        
        result = a_int - b_int
        
        return self.int_to_mang(result)

a = atrub([1, 2, 3])
b = atrub([1, 0, 1])
result = a.Tru(b)
print(result)
