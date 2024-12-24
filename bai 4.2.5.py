s = input().strip()

hoa = 0
thuong = 0
so = 0

for i in s:
    if i.isupper():
        hoa += 1
    elif i.islower():
        thuong += 1
    elif i.isdigit():
        so += 1

print(hoa, thuong, so)