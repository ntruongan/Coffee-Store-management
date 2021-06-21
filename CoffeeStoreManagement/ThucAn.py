from DSNL import *
class ThucAn:
    def __init__(self, MS, Ten, Gia, nl, sol):
        self._MaSo = MS
        self._Ten = Ten
        self._Gia = Gia
        self._NLieu = []
        self._NLieu.extend(nl)
        self._SoLuong = []
        self._SoLuong.extend(sol)
        self.tinhgiavon()


    def __getitem__(self, item):
        return self._Congthuc[item]

    def __setitem__(self, key, value):
        self._Congthuc[key] = value

    @property
    def sluong(self):
        return self._SoLuong

    @sluong.setter
    def sluong(self, value):
        self._SoLuong = value

    def __getitem__(self, item):
        return self._SoLuong[item]

    def __setitem__(self, key, value):
        self._SoLuong[key] = value

    @property
    def nlieu(self):
        return self._NLieu

    @nlieu.setter
    def nlieu(self, value):
        self._NLieu = value

    def __getitem__(self, item):
        return self._NLieu[item]

    def __setitem__(self, key, value):
        self._NLieu[key] = value

    @property
    def tienlai(self):
        return self._TienLai

    @tienlai.setter
    def tienlai(self, value):
        self._TienLai = value

    @property
    def gia(self):
        return self._Gia

    @gia.setter
    def gia(self, value):
        self._Gia = value

    @property
    def trangthai(self):
        return self._TrangThai

    @trangthai.setter
    def trangthai(self, value):
        self._TrangThai = value

    @property
    def giavon(self):
        return self._GiaVon

    @giavon.setter
    def giavon(self, value):
        self._GiaVon = value

    @property
    def ct(self):
        return self._Congthuc

    @ct.setter
    def ct(self, value):
        self._Congthuc = value

    @property
    def ten(self):
        return self._Ten

    @ten.setter
    def ten(self, value):
        self._Ten = value

    @property
    def ms(self):
        return self._MaSo

    @ms.setter
    def ms(self, value):
        self._MaSo = value

    def Xuat(self):
        print("ID {}: {}\t:{}".format(self.ms,self.ten,self.gia))

    def Xuatfile(self):
        a=[]            #list luu ms,ten,gia
        a.append(str(self.ten))
        a.append(":\t")
        a.append(str(self.gia))
        str1 = ''.join(a)
        return str1

    def KiemTraNL(self):
        for i in range(len(self.sluong)):
            if not self.nlieu[i].trangthai:
                return False
        return True



    def TruNL(self):
        for i in range(len(self.sluong)):
            self.nlieu[i].TruNL(self._SoLuong[i])

    def ThemNL(self):
        for i in range(len(self.sluong)):
            self.nlieu[i].NhapNL_x(self._SoLuong[i])

    def tinhgiavon(self):
        __k = []
        for x in range(len(self.sluong)):
            __k.append(self.nlieu[x].GiaNL)
        __von = [x1*x2 for (x1, x2) in zip(self._SoLuong, __k)]
        #print(self._SoLuong)
        self.giavon = sum(__von)

    def xuatCongThuc(self):
        nglieu = open("NguyenLieu.txt", "a+")
        print("Cong thuc mon {}: ".format(self.ten))
        nglieu.write("\nCong thuc mon {}: ".format(self.ten))
        __k = []
        for x in range(len(self.sluong)):
            __k.append(self.nlieu[x].tennl)
        for x,y in zip(__k, self.sluong):
            print("     {}: {}".format(x, y))
            nglieu.write("\n     {}: {}".format(x, y))
        nglieu.write("\n")
        nglieu.close()

'''
a = ThucAn(121, "Mi Xao", 20000, [DSNL.dsnl[0], DSNL.dsnl[1], DSNL.dsnl[2]], [2, 1, 2])
a.Xuat()

'''



