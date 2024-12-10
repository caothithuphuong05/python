import math
a, b, c = map(int, input().split())

delta = b * b - 4 * a * c

if delta > 0:
    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)
    print("{:.2f} {:.2f}".format(x1, x2))

elif delta == 0:
    x = -b / (2 * a)
    print("{:.2f}".format(x))

else:
    print("VN")
