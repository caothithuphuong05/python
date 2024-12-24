def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
n = int(input())
if n > 0:    
    ds_fib =  []
    for i in range (n):
        ds_fib.append(fib(i))
    tong = 0
    for j in ds_fib:
        print(j, end = " ")
        tong += j
    print()
    print(tong)
