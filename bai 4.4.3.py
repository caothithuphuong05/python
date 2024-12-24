with open('sach.txt', 'r') as file:  
    sach = file.readlines()

loc_sach = []

for i in range(0, len(sach), 3):  
    ten = sach[i].strip()
    trang = int(sach[i + 1].strip())
    gia = float(sach[i + 2].strip())

    if gia > 100000 and trang < 200:
        loc_sach.append(f"{ten}\n{trang}\n{gia}\n")

with open('ketqua.txt', 'w') as kq:  
    kq.writelines(loc_sach)
