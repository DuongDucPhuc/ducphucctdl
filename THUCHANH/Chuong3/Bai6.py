class Node:
    def __init__(self, he_so, so_mu):
        self.HeSo = he_so
        self.SoMu = so_mu
        self.KeTiep = None

class DaThuc:
    def __init__(self):
        self.Head = None

    def them_so_hang(self, he_so, so_mu):
        new_node = Node(he_so, so_mu)
        if not self.Head:
            self.Head = new_node
        else:
            current = self.Head
            while current.KeTiep:
                current = current.KeTiep
            current.KeTiep = new_node

    def hien_thi(self):
        current = self.Head
        while current:
            print(f"{current.HeSo}x^{current.SoMu}", end=" ")
            if current.KeTiep:
                print("+", end=" ")
            current = current.KeTiep
        print()

    def Chep(self):
        if not self.Head:
            return DaThuc()  
        
        
        new_dathuc = DaThuc()
        current = self.Head
        new_dathuc.Head = Node(current.HeSo, current.SoMu)
        new_current = new_dathuc.Head
        
        current = current.KeTiep
        while current:
            new_node = Node(current.HeSo, current.SoMu)
            new_current.KeTiep = new_node
            new_current = new_current.KeTiep
            current = current.KeTiep
        
        return new_dathuc
a = DaThuc()
a.them_so_hang(3, 2)
a.them_so_hang(2, 1)
a.them_so_hang(1, 0)
#sao chep' da thuc'
b = a.Chep()
print(b.hien_thi())
