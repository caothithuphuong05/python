import math

def ktra_so_hoan_hao(n):
    if n < 2:
        return False
    tong = 1  
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            tong += i
            if i != n // i:  
                tong += n // i
    return tong == n

def ktra_trong_khoang(a, b):
    so_hoan_hao = []
    for j in range(a + 1, b):
        if ktra_so_hoan_hao(j):
            so_hoan_hao.append(j)
    return so_hoan_hao

a, b = map(int, input().split())

so_hoan_hao = ktra_trong_khoang(a, b)

if so_hoan_hao:
    for k in so_hoan_hao:
        print(k, end=" ")
    print()
else:
    print("khong co so hoan hao")
