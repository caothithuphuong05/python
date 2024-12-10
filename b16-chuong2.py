import math

a, b, c = map(int, input().split())

if a + b > c or a + c > b or b + c > a:
    C = a + b + c
    p = C / 2
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print("{:.2f} {:.2f}".format(C, S))