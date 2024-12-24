def doi_10_sang_16(n):
    bang_16 = "0123456789ABCDEF"
    
    if n == 0:
        return "0"
    
    tlp = ""
    
    while n > 0:
        tlp = bang_16[n % 16] + tlp
        n //= 16
        return tlp
    
a = int(input())
if a > 0:
    he16 = doi_10_sang_16(a)
    print(he16)
