class NguyenLieu:

    def __init__(self, ten, maNL, gia, conlai):
        self._TenNL = ten
        self._MaNL = maNL
        self._GiaNL = gia
        self._ConLai = conlai
        self._TrangThai = True

    def __add__(self, other):
        self._ConLai += other

    def __sub__(self, other):
        self._ConLai -= other

    @property
    def conlai(self):
        return self._ConLai

    @conlai.setter
    def conlai(self, value):
        self._ConLai = value

    @property
    def soluong(self):
        return self._SL

    @soluong.setter
    def soluong(self, value):
        self._SL = value

    @property
    def trangthai(self):
        return self._TrangThai

    @trangthai.setter
    def trangthai(self, value):
        self._TrangThai = value

    @property
    def GiaNL(self):
        return self._GiaNL

    @GiaNL.setter
    def GiaNL(self, value):
        self._GiaNL = value

    @property
    def tennl(self):
        return self._TenNL

    @tennl.setter
    def tennl(self, value):
        self._TenNL = value

    @property
    def manl(self):
        return self._MaNL

    @manl.setter
    def manl(self, value):
        self._MaNL = value

    def Tinhgia(self):
        return self.GiaNL*self.soluong


    def NhapNL(self):
        k=int(input("Nhap so luong NL {} nhap: ".format(self.tennl)))
        self.__add__(k)

    def XuatThongTinNL(self):
        print("Ten: {}".format(self.tennl))
        print("Ma so: {}".format(self.manl))
        print("So Luong con lai: {}".format(self.conlai))

    def TruNL(self, x):
        if self.conlai - x >= 0:
            self.__sub__(x)
            self.trangthai = True
        else:
            print("Het Nguyen lieu: ")
            self.trangthai = False
'''
a=NguyenLieu("Banh tran","11",10000)
a.XuatThongTinNL()
a.NhapNL()
a.XuatThongTinNL()'''
'''    def NhapNL_x(self, x):
        self.conlai = self.conlai + x'''