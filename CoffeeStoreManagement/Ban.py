from DSSP import DSSP
import datetime
from QuanLyBase import QuanLy

class Ban(QuanLy):
    def __init__(self, soBan):
        self.__DSTA = []
        self.__timeIn = datetime
        self.__timeOUT = datetime
        self.__SoBan = soBan
        self.__TongTien = 0
        self.__Von = 0
        self.__Trangthai = False
        self.__dssp = DSSP()

    @property
    def dssp(self):
        return self.__dssp
    @dssp.setter
    def dssp(self, value):
        self.__dssp = value

    @property
    def trangthai(self):
        return self.__Trangthai
    @trangthai.setter
    def trangthai(self, value):
        self.__Trangthai = value

    @property
    def tongtien(self):
        return self.__TongTien
    @tongtien.setter
    def tongtien(self, value):
        self.__TongTien = value

    @property
    def IDban(self):
        return self.__SoBan
    @IDban.setter
    def IDban(self, value):
        self.__SoBan = value

    @property
    def timeout(self):
        return self.__timeOUT
    @timeout.setter
    def timeout(self, value):
        self.__timeOUT = value

    @property
    def thu(self):
        return self.__Thu

    @property
    def timein(self):
        return self.__timeIn
    @timein.setter
    def timein(self, value):
        self.__timeIn = value

    @property
    def dsta(self):
        return self.__DSTA
    @dsta.setter
    def dsta(self, value):
        self.__DSTA.extend(value)

    def __getitem__(self, item):
        return self.__DSTA[item]

    def __setitem__(self, key, value):
        self.__DSTA[key] = value

    def ThemMonID(self, id):
        if self.trangthai==True:
            item = next((x for x in self.dssp.danhsachSp if x.ms == id), None)
            #print(item.gia)
            if item != None:
                item.TruNL()
                if item.KiemTraNL():
                    self.dsta.append(item)
            else:
                print("ID khong ton tai")
        else:
            print("Ban nay chua duoc dat!!")

    def Them(self):
        if self.trangthai:
            for x in self.dssp.danhsachSp:
                x.Xuat()
            k = input("Nhap ID mon: ")
            self.ThemMonID(int(k))
            k = input("Tiep tuc Them mon an (y/n): ")
            if k.lower() == 'y':
                self.Them()
        else:
            print("Ban chua duoc dat")

    def XoaMonID(self,id):
        item = next((x for x in self.dsta if x.ms == id), None)
        if item == None:
            print("Khong ton tai ID trong Danh sach")
        else:
            item.ThemNL()
            self.dsta.remove(item)
            print("Xoa thanh cong: ")


    def Xoa(self):
        if self.trangthai:
            for x in self.dsta:
                x.Xuat()
            xoa = input("Nhap ID can xoa: ")
            self.XoaMonID(int(xoa))
        else:
            print("Ban chua duoc dat: ")


    def tinhTien(self):
        self.tongtien = 0
        for x in self.dsta:
            self.tongtien += x.gia

    def datBan(self):
        if(self.trangthai == False):
            self.timein = datetime.datetime.now()
            self.trangthai = True
            print("Dat ban thanh cong ")
        else:
            print("Ban da co khach dat")

    def Xuat(self):
        if self.trangthai:
            self.tinhTien()
            fl = open("Bill.txt", "a+")
            self.timeout = datetime.datetime.now()
            print("Hoa don in luc: {}".format(self.timeout.strftime("%D %H:%M")))
            print("")
            print("Ban so: {}".format(self.IDban))
            fl.write("\n-------------------------------------------------------------------\n")
            fl.write("Hoa don in luc: {}\n".format(self.timeout.strftime("%D %H:%M")))
            fl.write("Ban {}\n".format(self.IDban))
            for x in self.dsta:
                x.Xuat()
                fl.write(x.Xuatfile()+"\n")
            print("TONG CONG: {}".format(self.tongtien))
            fl.write("TONG CONG: {}".format(self.tongtien)+"\n")
            fl.write("-------------------------------------------------------------------\n")
            fl.close()
            #file luu tien thu
            fl2 = open("Thu.txt", "a+")
            fl2.write(format(self.tongtien)+"\n")
            self.trangthai = False
        else:
            print("Ban nay chua duoc dat!!")

    def QuanLy(self):
        print("\n------------------Ban so: {}----------------".format(self.IDban))
        print("|    1. Dat ban                             |\n"
              "|    2. Them mon                            |\n"
              "|    3. Xoa mon                             |\n"
              "|    4. Xuat Danh sach mon da goi           |\n"
              "|    5. Xuat Bill                           |\n"
              "|    6. Thoat                               |\n"
              "---------------------------------------------\n")

        k = input("Chon so theo menu: ")

        if k=='1':
            self.datBan()
            self.QuanLy()
        elif k=='2':
            self.Them()
            self.QuanLy()
        elif k=='3':
            self.Xoa()
            self.QuanLy()
        elif k=='4':
            if self.trangthai:
                if len(self.dsta)==0:
                    print("Chua goi mon")
                else:
                    print("\n\nDanh sach cac mon da dat: ")
                    for x in self.dsta:
                        x.Xuat()
                        #print("\n\n")
            else:
                print("Ban nay chua duoc dat: ")
                self.QuanLy()
        elif k=='5':
            self.Xuat()
            self.QuanLy()
        elif k=='6':
            return None
        else:
            print("Nhap lai du lieu: ")
            self.QuanLy()

'''b=Ban(112)
b.QuanLyBan()
print("ra roi ne")
'''