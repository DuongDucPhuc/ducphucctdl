class BieuThuc:
    def __init__(self, bt):
        self.bt = bt

    def do_uu_tien(self, toan_tu):
        if toan_tu in ('+', '-'):
            return 1
        elif toan_tu in ('*', '/'):
            return 2
        return 0

    def HauTo(self):
        toan_hang = []
        toan_tu = []

        i = 0
        while i < len(self.bt):
            if self.bt[i].isdigit():
                so = []
                while i < len(self.bt) and self.bt[i].isdigit():
                    so.append(self.bt[i])
                    i += 1
                toan_hang.append(''.join(so))
                continue
            elif self.bt[i] in "+-*/":
                while (toan_tu and self.do_uu_tien(toan_tu[-1]) >= self.do_uu_tien(self.bt[i])):
                    toan_hang.append(toan_tu.pop())
                toan_tu.append(self.bt[i])
            i += 1

        while toan_tu:
            toan_hang.append(toan_tu.pop())

        return ' '.join(toan_hang)

# Ví dụ sử dụng
bt = BieuThuc('2 + 3 * 5')
print(bt.HauTo())  # Kết quả: '2 3 5 * +'
