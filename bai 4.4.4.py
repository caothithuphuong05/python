class NhanVien:
   
    def __init__(self):
        self.name = ""
        self.ma = 0
        self.hs = 0.0
        self.pc = 0

    def nhap(self):
        self.name, self.ma, self.hs, self.pc = input().split()
        self.ma = int(self.ma)
        self.hs = float(self.hs)
        self.pc = int(self.pc)
        self.luong = self.hs * 2000000 + self.pc

    def xuat(self):
        print("{0} {1} {2:.2f} {3} {4:.2f}".format(self.ma, self.name, self.hs, self.pc, self.luong))

n = int(input())
ds = []

for i in range(n):
    nv = NhanVien()
    nv.nhap()
    ds.append(nv)

nv_luong_thap_nhat = min(ds, key=lambda nv: nv.luong)

print("Nhan vien co luong thap nhat")
nv_luong_thap_nhat.xuat()
