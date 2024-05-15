class TuDien:
    def __init__(self):
        self.du_lieu = {}

    def NhapTu(self, tu, dongnghia, trainghia):
        self.tu = tu
        self.dongnghia = None
        self.trainghia = None
        khoa_bam = self._HamBam(tu)
        if khoa_bam not in self.du_lieu:
            self.du_lieu[khoa_bam] = {'tu': tu, 'dong_nghia': [], 'trai_nghia': []}
        if dongnghia:
            self.du_lieu[khoa_bam]['dong_nghia'].extend(dongnghia)
        if trainghia:
            self.du_lieu[khoa_bam]['trai_nghia'].extend(trainghia)

    def dong_nghia(self, tu):
        khoa_bam = self._HamBam(tu)
        if khoa_bam in self.du_lieu and tu in self.du_lieu[khoa_bam]:
            return self.du_lieu[khoa_bam][tu]['dong_nghia']
        else:
            return []
    def trai_nghia(self, tu):
        khoa_bam = self._HamBam(tu)
        if khoa_bam in self.du_lieu and tu in self.du_lieu[khoa_bam]:
            return self.du_lieu[khoa_bam][tu]['trai_nghia']
        else:
            return []
    def _HamBam(self, tu):
        return tu[0].lower()
td = TuDien()
td.NhapTu('nhanh', dongnghia =['tốc độ', 'mau le'],trainghia=['chậm'])
td.NhapTu('chậm', dongnghia=['slow', 'từ từ'], trainghia=['nhanh'])


tudongnghia = td.dong_nghia('nhanh')
print(tudongnghia)
tutrainghia =  td.trai_nghia('chậm')
print(tutrainghia)