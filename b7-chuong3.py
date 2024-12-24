def tong(n):
    tong = 0
    n = abs(n)
    while n > 0:
        tong += n % 10 
        n //= 10
    return tong

n = int(input())
kq = tong(n)
print(kq)
