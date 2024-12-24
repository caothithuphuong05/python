def check_matrix_type():
    n = int(input())

    mt = []
    for _ in range(n):
        row = list(map(int, input().split()))
        mt.append(row)

    tam_giac_tren = True
    tam_giac_duoi = True

    for i in range(n):
        for j in range(n):
            if i > j and mt[i][j] != 0:
                tam_giac_tren = False
            if i < j and mt[i][j] != 0:
                tam_giac_duoi = False

    if tam_giac_tren:
        print("UPPER TRIANGLE")
    elif tam_giac_duoi:
        print("LOWER TRIANGLE")
    else:
        print("NONE")

check_matrix_type()
