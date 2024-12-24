def doi_10_sang_2(n):
    if n == 0:
        return "0"
    
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary  
        n //= 2
    return binary

n = int(input())
if n > 0:
    he2 = doi_10_sang_2(n)
    print(he2)