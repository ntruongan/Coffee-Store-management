from NhanVien import NV
class TapVu(NV):
    def __init__(self, ten, ms, lzuongcb, gizolam):
        super().__init__(ten, ms, lzuongcb, gizolam)


    def Xuat(self):
        print("-------------Chuc vu: Tap vu-------------")
        super().Xuat()

    def tinhluong(self):
        self.luongct = self.luongcb*self.gio + 250000