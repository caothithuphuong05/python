import re

s = input().strip()
so = re.findall(r'\d+', s)
so = [str(int(num)) for num in so]
sx = sorted(so, key=int)

duyet_so = iter(sx)

kq = re.sub(r'\d+', lambda _: next(duyet_so), s)

print(kq)
    