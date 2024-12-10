import math
n = int(input())
x = float(input())

S =x
for i in range(n):
    S = math.sqrt(x + S)

print("{:.2f}".format(S))