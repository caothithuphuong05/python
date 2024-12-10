import math

def ktra_so_nguyen_to(a):
    if a < 2:
        return 0
    
    for i in range(2, int(math.sqrt(a) + 1)):
        if a % i == 0:
            return 0
    return 1

def trong_khoang(n):
    so_nguyen_to = []
    
    for i in range(1, n + 1):
        if ktra_so_nguyen_to(i):
            so_nguyen_to.append(i)
    return so_nguyen_to

n = int(input())
so_nguyen_to = trong_khoang(n)

for i in so_nguyen_to:  
    print(i, end = " ")
print()
