m, n, k = map(int, input().split())

mt = []
for i in range(m):
    hang = list(map(int, input().split()))
    mt.append(hang)

dem = 0
for hang in mt:
    dem += hang.count(k)

print(dem)