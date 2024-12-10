import math
n = int(input())

S = 0
for i in range(1, 2 * n + 2):
    if i % 2 != 0:
        S += 1/(math.factorial(i))
print(S)
