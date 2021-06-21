from ThucAn import ThucAn
from DSNL import DSNL


class DSSP:
    def __init__(self):
        self.__danhsachSP = []
        self.__danhsachSP.append(ThucAn(111, "Banh Bong Lan", 20000, [DSNL.dsnl[18]], [1]))
        self.__danhsachSP.append(ThucAn(112, "Banh Flan", 25000, [DSNL.dsnl[19]], [1]))
        self.__danhsachSP.append(ThucAn(121, "Mi Xao", 20000, [DSNL.dsnl[0], DSNL.dsnl[1], DSNL.dsnl[2]], [2, 1, 2]))
        self.__danhsachSP.append(ThucAn(122, "Com Cuon", 35000, [DSNL.dsnl[3]], [5]))
        self.__danhsachSP.append(ThucAn(123, "Kho ga", 15000, [DSNL.dsnl[4]], [250]))
        self.__danhsachSP.append(ThucAn(211, "Ca Phe Den", 22000, [DSNL.dsnl[5]], [450]))
        self.__danhsachSP.append(ThucAn(212, "Ca Phe Sua", 22000, [DSNL.dsnl[5], DSNL.dsnl[6]], [400, 200]))
        self.__danhsachSP.append(ThucAn(213, "Bac Siu", 25000, [DSNL.dsnl[5], DSNL.dsnl[6]], [200, 400]))
        self.__danhsachSP.append(ThucAn(221, "Tra Sen", 22000, [DSNL.dsnl[8]], [150]))
        self.__danhsachSP.append(ThucAn(222, "Tra Vai", 30000, [DSNL.dsnl[8], DSNL.dsnl[9]], [150, 2]))
        self.__danhsachSP.append(ThucAn(223, "Tra Dao", 30000, [DSNL.dsnl[8], DSNL.dsnl[10]], [100, 2]))
        self.__danhsachSP.append(ThucAn(231, "Tra Sua Truyen Thong", 40000,  [DSNL.dsnl[20], DSNL.dsnl[16]], [150, 50]))
        self.__danhsachSP.append(ThucAn(232, "Tra Sua nhieu Toping", 50000, [DSNL.dsnl[20], DSNL.dsnl[11], DSNL.dsnl[12],
                                                                             DSNL.dsnl[13], DSNL.dsnl[14], DSNL.dsnl[15]], [200, 40, 40, 40, 40, 40]))
        self.__danhsachSP.append(ThucAn(233, "Sua tuoi Duong Den", 40000, [DSNL.dsnl[7], DSNL.dsnl[17]], [300, 100]))

    @property
    def danhsachSp(self):
        return self.__danhsachSP
    @danhsachSp.setter
    def danhsachSp(self, value):
        self.__danhsachSP = value

    def __getitem__(self, item):
        return self.__danhsachSP[item]

    def __setitem__(self, key, value):
        self.__danhsachSP[key] = value

    def xuatds(self):
        for x in self.danhsachSp:
            x.Xuat()
