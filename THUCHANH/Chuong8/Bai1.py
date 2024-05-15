class TuDien:
    def __init__(self):
        self.du_lieu = {}

    def NhapTu(self, tu, dong_nghia=None, trai_nghia=None):
        khoa_bam = self._HamBam(tu)
        if khoa_bam not in self.du_lieu:
            self.du_lieu[khoa_bam] = {'tu': tu, 'dong_nghia': [], 'trai_nghia': []}
        if dong_nghia:
            self.du_lieu[khoa_bam]['dong_nghia'].append(dong_nghia)
        if trai_nghia:
            self.du_lieu[khoa_bam]['trai_nghia'].append(trai_nghia)

    def TraTu(self, tu):
        khoa_bam = self._HamBam(tu)
        if khoa_bam in self.du_lieu:
            return self.du_lieu[khoa_bam]['dong_nghia'], self.du_lieu[khoa_bam]['trai_nghia']
        else:
            return None, None

    def _HamBam(self, tu):
        return tu[0].lower()
td = TuDien()
td.NhapTu('nhanh', 'chậm', 'slow')
td.NhapTu('chậm', 'từ từ', 'nhanh')


tudongnghia = td.TraTu('nhanh')
print(tudongnghia)
tutrainghia =  td.TraTu('chậm')
print(tutrainghia)