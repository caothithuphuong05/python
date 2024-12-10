import math

ep = float(input())
x = float(input())

if 0 < ep < 1:
    term = 1  
    S = term  
    n = 0     

    while abs(term) >= ep:
        n += 1
        term *= x / n  
        S += term      
    print("{:.2f}".format(S))

