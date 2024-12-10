import math
n = int(input())

if n > 0:
    for i in range(2, math.sqrt(n) + 1):
        if n % i == 0:
            print("KHONG LÀ SO NGUYEN TO")
        else:
            print("N LA SO NGUYEN TO")
            print(" ", n)