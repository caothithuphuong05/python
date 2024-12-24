def ma_thuat(A, m, n):
    hang_ma_thuat = []
    for i in range(m):
        if sum(A[i]) % 7 == 0:
            hang_ma_thuat.append(i+1)
    return hang_ma_thuat

m, n = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(m)]

so_hang = ma_thuat(A, m, n)
if so_hang:
    for i in so_hang:
        print(i)
else: 
    print("NO")