class NV:
    def __init__(self, ten, ms, luongcb, gio):
        self._Ten = ten
        self._MSNV = ms
        self._luongCB = luongcb
        self._luongCT = 0
        self._gio = gio

    @property
    def gio(self):
        return self._gio
    @gio.setter
    def gio(self, value):
        self._gio = value

    @property
    def luongct(self):
        return self._luongCT
    @luongct.setter
    def luongct(self, value):
        self._luongCT = value

    @property
    def luongcb(self):
        return self._luongCB
    @luongcb.setter
    def luongcb(self, value):
        self._luongCB = value

    @property
    def tennv(self):
        return self._Ten
    @tennv.setter
    def tennv(self,value):
        self._Ten = value

    @property
    def msnv(self):
        return self._MSNV
    @msnv.setter
    def msnv(self, value):
        self._MSNV = value

    def tinhluong(self):
        return self.luongcb

    def Xuat(self):
        print("~~Ten NV: {}".format(self.tennv))
        print("~~Ma so NV: {}".format(self.msnv))

    def Nhap(self):
        q = input("Nhap Ten NV: ")
        self.tennv = q
        w = input("Nhap Ma so NV: ")
        self.msnv = w
        e = input("Nhap Luong CB: ")
        self.luongcb = e
        r = input("Nhap so gio lam viec: ")
        self.gio = r
