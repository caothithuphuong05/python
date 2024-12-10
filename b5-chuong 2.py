a1, b1, c1 = map(int,input().split())
a2, b2, c2 = map(int,input().split())

D = a1 * b2 - a2 * b1
D1 = c1 * b2 - c2 * b2
D2 = a1 * c2 - a2 * c1

if D == 0:
    if D1 == 0 and D2 == 0:
        print("VSN")
    else:
        print("VN")
else:
    x = D1 / D
    y = D2 / D
    print("x = {:.2f}\ny = {:.2f}".format(x, y))
    