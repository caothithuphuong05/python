def tim_x_trong_a(a, x):
    return x in a
            
n, k = map(int, input().split())
a = list(map(int, input().split()))
x = list(map(int, input().split()))

a = set(a)

for i in x:
    if tim_x_trong_a(a, i):
        print("YES")
    else:
        print("NO")