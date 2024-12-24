s = input().strip()

numbers = s.split(',')

sole = []

for num in numbers:
    num = num.strip()
    if num:  
        num = int(num)
        if num % 2 != 0:
            sole.append(num)

print(" ".join(map(str, sole)))