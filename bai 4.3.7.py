def tong_cheo_chinh_phu(A, n):
    chinh = 0
    phu = 0
    for i in range(n):
        chinh += A[i][i]
        phu += A[i][n - i - 1]

    return chinh, phu

n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

tong_chinh, tong_phu = tong_cheo_chinh_phu(A, n)
print(tong_chinh)
print(tong_phu)