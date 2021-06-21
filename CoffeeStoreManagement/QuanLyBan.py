from Ban import Ban
from DSNL import DSNL


class Qly():
    def __init__(self):
        self.__DSB = [Ban(100), Ban(101), Ban(102), Ban(103), Ban(104),
                     Ban(105), Ban(106), Ban(107), Ban(108), Ban(109)]
        self.__Thu = 0
        self.__Chi = 0
        #self.__DSNLieu = DSNL
    @property
    def dsb(self):
        return self.__DSB
    @dsb.setter
    def dsb(self, value):
        self.__DSB = value

    def __getitem__(self, item):
        return self.__DSB[item]

    def __setitem__(self, key, value):
        self.__DSB[key] = value

    def XuatDanhSachBanTrong(self):
        print("Danh sach ban trong: ")
        for x in self.__DSB:
            if not x.trangthai:
                print("\tBan so: {}".format(x.IDban))

    def XuatDanhSachBan(self):
        print("Danh sach ban : ")
        for x in self.__DSB:
            if not x.trangthai: #chua duoc dat
                print("\tBan so: {}".format(x.IDban))
            else:
                print("\tBan so: {} (da duoc dat)".format(x.IDban))

    def DatBanID(self, id):
        for x in self.dsb:
            if x.IDban == id:
                x.datBan()

    def Quanly(self):
        self.XuatDanhSachBan()
        k = int(input("Nhap id Ban: "))
        for x in self.dsb:
            if x.IDban == k:
                x.QuanLy()

    def TongThu(self):
        self.__Thu = 0
        with open("Thu.txt") as search:
            for line in search:
                line = line.rstrip()  # remove '\n' at end of line
                self.__Thu += int(line)
        print("TONG THU: {}".format(self.__Thu))

    def TongChi(self):
        self.__Chi = 0
        with open("Chi.txt") as search:
            for line in search:
                line = line.rstrip()  # remove '\n' at end of line
                self.__Chi += int(line)
        print("TONG CHI: {}".format(self.__Chi))

    def menu(self):
        print(">>>>>>>>>>>>>>>>MENU<<<<<<<<<<<<<<\n"
              "|    1. Quan ly Ban              |\n"
              "|    2. Quan ly Nguyen Lieu      |\n"
              "|    3. Quan ly Tong Thu/Chi     |\n"
              "|    4. Thoat                    |\n"
              "----------------------------------\n")
        k = input("Chon so theo menu: ")
        if k == '1':
            self.Quanly()
            self.menu()
        elif k == '2':
            DSNL.QuanLy()
            self.menu()
        elif k == '3':
            self.TongThu()
            self.TongChi()
            print("Tien Lai: {}".format(self.__Thu-self.__Chi))
            self.menu()
        elif k == '4':
            return None




'''a = Qly()
a.menu()
'''