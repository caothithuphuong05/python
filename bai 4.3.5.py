m, n = map(int, input().split())  
mt = []
tong = 0

for i in range(m):
    row = list(map(int, input().split()))  
    mt.append(row)
    tong += sum(row)  

tong_so_phan_tu = m * n
tbc = tong / tong_so_phan_tu

print(f"{tbc:.2f}")

for i in range(m):
    for j in range(n):
        if mt[i][j] > tbc:
            print(mt[i][j], i + 1, j + 1)
