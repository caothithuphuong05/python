import math

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
x3, y3 = map(float, input().split())

S = 1/2 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

if S == 0:
    print("khong la tam giac")
else:
    c1 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    c2 = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)
    c3 = math.sqrt((x2 - x3)**2 + (y2 - y3)**2)
    C = c1 + c2 + c3
    print("{:.2f} {:.2f}".format(S, C))

   