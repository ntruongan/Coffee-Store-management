from NguyenLieu import NguyenLieu
from QuanLyBase import QuanLy


class DSNL(QuanLy):
    dsnl = [NguyenLieu("Mi Cuon", "00", 1500, 0), NguyenLieu("Trung", "01", 700, 150),
                    NguyenLieu("Xuc xich", "02", 5000, 100), NguyenLieu("Cuon Com", "03", 10000, 100),
                    NguyenLieu("Kho ga", "04", 50, 5000), NguyenLieu("Ca Phe", "05", 20, 10000), NguyenLieu("Sua", "06", 30, 10000),
                    NguyenLieu("Sua tuoi", "07", 60,10000), NguyenLieu("Tra", "08", 100,10000), NguyenLieu("Vai", "09", 12, 10000),
                    NguyenLieu("Dao", "10", 5000,10000), NguyenLieu("Topping Thuy Tinh", "11", 20, 2000),
                    NguyenLieu("Topping Pho Mai", "12", 20, 2000), NguyenLieu("Topping Pha Le", "13", 20, 2000),
                    NguyenLieu("Topping Thach Dua", "14", 20, 2000), NguyenLieu("Topping Pudding", "15", 20, 2000),
                    NguyenLieu("Tran chau", "16", 30, 3000), NguyenLieu("Tran chau duong den", "17", 30, 3000),
                    NguyenLieu("Banh Bong lan", "18", 15000, 40), NguyenLieu("Banh Flan", "19", 15000, 40),
                    NguyenLieu("Tra Sua", "20", 200, 10000)]

    @classmethod
    def Xuat_ID(cls, id):
        item = next((x for x in cls.dsnl if x.manl == id), None)
        if not item is None:
            item.XuatThongTinNL()
        else:
            print("Sai ID\n")
            cls.Xuat()

    @classmethod
    def Xuat(cls):
        print("\n-----------DANH SACH NGUYEN LIEU-----------\n"
              "|\t1. Xuat toan bo danh sach Nguyen lieu|\n"
              "|\t2. Xuat Nguyen lieu da het           |\n"
              "|\t3. Xuat theo ID                      |\n"
              "|\t4. Thoat                             |")
        __q = input("Chon menu: ")
        if __q == '1':
            for x in DSNL.dsnl:
                x.XuatThongTinNL()
            cls.QuanLy()
        elif __q=='2':
            cls.Xuat_NLdaHet()
            cls.QuanLy()
        elif __q == '3':
            __k=input("Nhap ID: ")
            cls.Xuat_ID(__k)
            cls.QuanLy()
        elif __q == '4':
            return None
        else:
            print("Nhap lai: ")
            cls.Xuat()

    @classmethod
    def ThemNL_ID(cls, id):
        item = next((x for x in cls.dsnl if x.manl == id), None)
        if item != None:
            __sl = int(input("Nhap so luong them: "))
            item.conlai += __sl
            #ghi file
            fl = open("Chi.txt", "a+")
            __gia=int(item.GiaNL)*int(__sl)
            fl.write(format(__gia)+"\n")
            fl.close()
        else:
            print("ID khong ton tai")
            cls.Them()

    @classmethod
    def Them(cls):
        __k = input("Nhap ID Nguyen Lieu: ")
        cls.ThemNL_ID(__k)

    @classmethod
    def Xoa(cls):
        __k = input("Nhap ID Nguyen Lieu: ")
        cls.XoaNL_ID(__k)

    @classmethod
    def XoaNL_ID(cls):
        item = next((x for x in cls.dsnl if x.manl == id), None)
        if item != None:
            __sl = int(input("Nhap so luong xoa: "))
            item.conlai -= __sl
        else:
            print("ID khong ton tai")
            cls.Xoa()

    @classmethod
    def Xuat_NLdaHet(cls):
        item = next((x for x in cls.dsnl if x.trangthai == False), None)
        if item != None:
            item.XuatThongTinNL()
        else:
            print("\nKhong co Nguyen lieu da het!\n")
    @classmethod
    def QuanLy(cls):
        print("\n---------QUAN LY NGUYEN LIEU-----------\n"
              " |\t1. Xuat Danh sach Nguyen lieu        |\n"
              " |\t2. Them Nguyen Lieu                  |\n"
              " |\t3. Tru Nguyen Lieu                   |\n"
              " |\t4. Thoat                             |\n")
        __n = input("Chon menu: \n")
        if __n == '1':
            cls.Xuat()
            cls.QuanLy()
        elif __n == '2':
            cls.Them()
            cls.QuanLy()
        elif __n == '3':
            cls.Xoa()
            cls.QuanLy()
        elif __n == '4':
            print("Thoat")
            return None
        else:
            print("Nhap lai: ")
            cls.QuanLy()


'''
            
    def
    def __init__(self):
        self.__dsnl = [NguyenLieu("Mi Cuon", "00", 1500, 160), NguyenLieu("Trung", "01", 700, 150),
                    NguyenLieu("Xuc xich", "02", 5000, 100), NguyenLieu("Cuon Com", "03", 10000, 100),
                    NguyenLieu("Kho ga", "04", 50, 5000), NguyenLieu("Ca Phe", "05", 20, 10000), NguyenLieu("Sua", "06", 30, 10000),
                    NguyenLieu("Sua tuoi", "07", 60,10000), NguyenLieu("Tra", "08", 100,10000), NguyenLieu("Vai", "09", 12, 10000),
                    NguyenLieu("Dao", "10", 5000,10000), NguyenLieu("Topping Thuy Tinh", "11", 20, 2000),
                    NguyenLieu("Topping Pho Mai", "12", 20, 2000), NguyenLieu("Topping Pha Le", "13", 20, 2000),
                    NguyenLieu("Topping Thach Dua", "14", 20, 2000), NguyenLieu("Topping Pudding", "15", 20, 2000),
                    NguyenLieu("Tran chau", "16", 30, 3000), NguyenLieu("Tran chau duong den", "17", 30, 3000),
                    NguyenLieu("Banh Bong lan", "18", 15000, 40), NguyenLieu("Banh Flan", "19", 15000, 40),
                    NguyenLieu("Tra Sua", "20", 200, 10000)]

    @property
    def danhsachNl(self):
        return self.__dsnl

    @danhsachNl.setter
    def danhsachNl(self, value):
        self.__dsnl = value

    def __getitem__(self, item):
        return self.__dsnl[item]

    def __setitem__(self, key, value):
        self.__dsnl[key] = value'''
'''
    @classmethod
    def XuatDSNL(cls):
        print("-----------DANH SACH NGUYEN LIEU-----------")
        for x in DSNL.dsnl:
            x.XuatThongTinNL()
            print()'''
'''DSNL.QuanLy()
DSNL.Xuat()'''