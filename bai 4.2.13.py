def chay_code(s):
    ma_hoa = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:  
            count += 1
        else:
            ma_hoa.append(f"{s[i - 1]}{count}")
            count = 1  
    if s:
        ma_hoa.append(f"{s[-1]}{count}")

    return ''.join(ma_hoa)

T = int(input())
results = []

for _ in range(T):
    S = input()
    results.append(chay_code(S))

for res in results:
    print(res)
