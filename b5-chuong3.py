def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def bcnn(a, b):   
    bcnn = int(abs(a * b) / ucln(a, b))
    return bcnn

a, b = map(int, input().split())
bcnn = bcnn(a, b)
print(bcnn)