def mt_doi_xung(A, n):
    for i in range(n):
        for j in range(n):
            if A[i][j] != A[j][i]:
                return 0
    return 1
            
n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

if mt_doi_xung(A, n):
    print("YES")
else:
    print("NO")