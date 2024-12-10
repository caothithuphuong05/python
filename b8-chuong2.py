x, n = map(int, input().split())

S = x * ((1 - x**n) / (1- x))

print("{:.2f}".format(S))