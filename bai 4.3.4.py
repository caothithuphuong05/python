def tong_ma_tran(A, B, m, n):
    C = [[0] * n for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C

m, n = map(int, input(). split())

A = [list(map(int, input(). split())) for _ in range(m)]
B = [list(map(int, input(). split())) for _ in range(m)]
C = tong_ma_tran(A, B, m, n)

for row in C:
    print(" ".join(map(str, row)))