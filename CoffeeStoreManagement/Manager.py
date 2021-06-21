from NhanVien import NV
from QuanLyBan import *

class ThuNgan(NV):
    def __init__(self, ten, ms, lzuongcb, gizolam, matkhau):
        super().__init__(ten, ms, lzuongcb, gizolam)
        self.__MK = matkhau

    @property
    def passw(self):
        return self.__MK

    def Xuat(self):
        print("Chuc vu: Thu Ngan")
        super().Xuat()

    def tinhluong(self):
        self.luongct = self.luongcb*self.gio

    def Quanly(self):
        qlb = Qly()
        qlb.menu()

'''    def QuanLyNV(self):
        print("\n=====Menu Quan ly Nhan vien=======\n"
              "1. Xuat Nhan Vien\n"
              "2. Them Nhan vien\n"
              "3. Xoa Nhan Vien\n")'''

