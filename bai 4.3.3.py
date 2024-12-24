def nhan_ma_tran(A, B, m, n, p):
    C = [[0] * p for _ in range(m)]

    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

m, n ,p = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(m)]
B = [list(map(int, input().split()) )for _ in range(n)]
C = nhan_ma_tran(A, B, m, n, p)

for row in C:
    print(" ".join(map(str, row)))