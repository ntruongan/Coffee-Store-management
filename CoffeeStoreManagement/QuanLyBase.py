from abc import ABC, abstractmethod


class QuanLy(ABC):
    @abstractmethod
    def Them(self):
        pass

    @abstractmethod
    def Xoa(self):
        pass

    @abstractmethod
    def Xuat(self):
        pass

    @abstractmethod
    def QuanLy(self):
        pass

