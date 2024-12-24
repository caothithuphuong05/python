class SinhVien:

    def __init__(self):
        self.name = ""
        self.ma = 0
        self.toan = 0
        self.triet = 0
        self.ltc = 0

    def nhap(self):
        self.name, self.ma, self.toan, self.triet, self.ltc = input().split()
        self.ma = int(self.ma)
        self.toan = float(self.toan)
        self.triet = float(self.triet)
        self.ltc = float(self.ltc)
        self.dtb = (self.toan + self.triet + self.ltc) / 3

    def xuat(self):
        print("{0} {1} {2:.2f} {3} {4:.2f}".format(self.ma, self.name, self.toan, self.triet, self.ltc, self.dtb))

    def hoc_lai(self):
        dem = sum(1 for i in[self.toan, self.triet, self.ltc] if i < 4.0)
        return dem >= 2

n = int(input())
ds = []
dem = 0

for i in range(n):
    sv = SinhVien()
    sv.nhap()
    if sv.hoc_lai():
        ds.append(sv)
        dem += 1

print("Danh sach sinh vien hoc lai")

for sv in ds:
    sv.xuat()

print(f"Danh sach nay co {dem} sinh vien phai hoc lai")
     
