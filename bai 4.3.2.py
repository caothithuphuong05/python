def tong_hieu(A, B, m, n):
    C = [[0] * n for _ in range(m)]
    D = [[0] * n for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
            D[i][j] = A[i][j] - B[i][j]
    return C, D

m, n = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(m)]
B = [list(map(int, input().split())) for _ in range(m)]

C, D = tong_hieu(A, B, m, n)

for row in C:
    print(" ".join(map(str, row)))

for row in D:
    print(" ".join(map(str, row)))

