def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a, b = map(int, input().split())
ucln = ucln(a, b)
print(ucln)