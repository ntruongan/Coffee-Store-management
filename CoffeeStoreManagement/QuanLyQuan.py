from Manager import ThuNgan
from BaoVe import Baove
from TapVu import TapVu
class Coffee:
    __DSTN = []
    __DSTN.append(ThuNgan("Nguyen Truong An", "18110246", 200000, 120, "2424924279"))
    __DSTN.append(ThuNgan("Nguyen Hoang Huy", "18110293", 200000, 120, "1234567890"))
    __DSBV = []
    __DSTV = []
    __DSBV.append(Baove("Nguyen Van Le", "18242525", 100000, 120))
    __DSBV.append(Baove("Tran Ngoc Le", "1722525", 100000, 120))
    __DSTV.append(TapVu("Nguyen Huy Ngoc", "18268264", 80000, 120))
    __DSTV.append(TapVu("Nguyen Huy Hoang", "18428774", 80000, 120))
    __DSTV.append(TapVu("Le Huy Khanh", "15128264", 80000, 120))
    __DSTV.append(TapVu("Ngo Tran Luong", "15228572", 80000, 120))

    @classmethod
    def QuanLyChung(cls,item):
        print("..............QUAN LY QUAN CA PHE............\n"
              "~~\t1. Quan ly Nhan vien                    ~~\n"
              "~~\t2. Quan ly Ban va Nguyen Lieu           ~~\n"
              "~~\t3. Thoat                                ~~\n")
        __u = input("Chon menu: ")
        if __u == '1':
            cls.MenuQuanLyNV(item)
            cls.DangNhap()
        elif __u == '2':
            item.Quanly()
            cls.DangNhap()
        elif __u == '3':
            cls.QuanLyChung(item)

    @classmethod
    def DangNhap(cls):
        __i=input("Nhap ma so Nhan vien cua ban: ")
        item = next((x for x in cls.__DSTN if x.msnv == __i), None)
        if not item is None:
            __j = input("Nhap Mat Khau: ")
            if item.passw == __j:
                item.Xuat()
                cls.QuanLyChung(item)
                cls.DangNhap()
            else:
                print("Sai mat khau!")
                cls.DangNhap()
        else:
            print("Khong ton tai Nhan vien")
            cls.DangNhap()

    @classmethod
    def ThemNVBaove(cls):
        a = Baove('','','','')
        a.Nhap()
        cls.__DSBV.append(a)

    @classmethod
    def XuatBaove(cls):
        for x in cls.__DSBV:
            x.Xuat()


    @classmethod
    def XoaNVBaove_ID(cls,id):
        #item = next( x for x in cls.__DSBV)
        item = next((x for x in cls.__DSBV if x.msnv == id), None)
        if not item is None:
            cls.__DSBV.remove(item)
        else:
            print("Khong ton tai ID:")


    @classmethod
    def XoaNVBaove(cls):
        cls.XuatBaove()
        __k=input("Nhap ID bao ve can xoa: ")
        cls.XoaNVBaove_ID(__k)

    @classmethod
    def ThemNVTapvu(cls):
        a1 = TapVu('','','','')
        a1.Nhap()
        cls.__DSTV.append(a1)

    @classmethod
    def XuatTapVu(cls):
        for x in cls.__DSTV:
            x.Xuat()


    @classmethod
    def XoaNVTapvu_ID(cls,id):
        #item = next( x for x in cls.__DSBV)
        item = next((x for x in cls.__DSTV if x.msnv == id), None)
        if not item is None:
            cls.__DSTV.remove(item)
        else:
            print("Khong ton tai ID:")


    @classmethod
    def XoaNVTapvu(cls):
        cls.XuatTapVu()
        __k=input("Nhap ID bao ve can xoa: ")
        cls.XoaNVTapvu_ID(__k)


    @classmethod
    def MenuQuanLyNV(cls,item):
        print("\n=====Menu Quan ly Nhan vien=======\n"
              " 1. Xuat Nhan Vien\n"
              " 2. Them Nhan vien\n"
              " 3. Xoa Nhan Vien\n"
              " 4. Thoat\n")
        __in = input("Chon menu: ")
        if __in == '1':
            print("1. Xuat Bao ve\n"
                  "2. Xuat Tap vu\n")
            i = input("Chon menu: ")
            if i == '1':
                cls.XuatBaove()
                cls.MenuQuanLyNV(item)
            elif i == '2':
                cls.XuatTapVu()
                cls.MenuQuanLyNV()
        elif __in == '2':
            print("1. Them Bao ve\n"
                  "2. Them Tap vu\n")
            i = input("Chon menu: ")
            if i == '1':
                cls.ThemNVBaove()
                cls.MenuQuanLyNV()
            elif i == '2':
                cls.ThemNVTapvu()
                cls.MenuQuanLyNV()
        elif __in == '3':
            print("1. Xoa Bao ve\n"
                  "2. Xoa Tap vu\n")
            i = input("Chon menu: ")
            if i == '1':
                cls.XuatBaove()
                cls.XoaNVBaove()
                cls.MenuQuanLyNV(item)
            elif i == '2':
                cls.XuatTapVu()
                cls.XoaNVTapvu()
                cls.MenuQuanLyNV(item)
        else:
            cls.QuanLyChung(item)

'''
    @classmethod
    def MenuQuanLyNV(cls):
        print("..............QUAN LY QUAN CA PHE............"
              "~~\t1. Quan ly Nhan vien                    ~~\n"
              "~~\t2. Quan ly Ban va Nguyen Lieu           ~~\n")
        __in=input("Chon menu: ")
        if __in == '2':
            cls.'''
Coffee.DangNhap()