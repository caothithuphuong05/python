import re
s = input().strip()
a = re.findall(r'\d+', s)
b = list(map(int, a))
x = max(b)
print(x)
