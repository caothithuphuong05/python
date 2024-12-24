s = input().strip()

def sua(s):
    words = s.split()
    viet_hoa = [word.capitalize() for word in words]
    return ' '.join(viet_hoa)

print(sua(s))