class Sach:
    def __init__(self, ten_sach, so_trang, gia_tien):
        self.ten_sach = ten_sach
        self.so_trang = so_trang
        self.gia_tien = gia_tien

    def gia_tb(self):
        return self.gia_tien / self.so_trang if self.so_trang != 0 else 0

    def nhap(self):
        self.ten_sach = input()
        self.so_trang = int(input())
        self.gia_tien = float(input())

    def xuat(self):
        return f"{self.ten_sach} {self.so_trang} {self.gia_tien:.2f} {self.gia_tb():.2f}"

def sx_theo_gia_tb(sach_list):
    sach_list.sort(key=lambda x: (x.gia_tb(), x.ten_sach))

def luu_kq(sach_list, filename="sach.txt"):
    with open(filename, "w") as file:
        for sach in sach_list:
            file.write(sach.xuat() + "\n")

n = int(input())
sach_list = []

for i in range(n):
    sach = Sach("", 0, 0)
    sach.nhap()
    sach_list.append(sach)

sx_theo_gia_tb(sach_list)
luu_kq(sach_list)
