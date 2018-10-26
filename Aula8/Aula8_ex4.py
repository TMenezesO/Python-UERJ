def Newton_sqrt(n):
    approx = n
    melhor = (approx + n/approx)/2
    while melhor != approx:
        approx = melhor
        melhor = (approx + n/approx)/2
        print (melhor)
    
Newton_sqrt(25)
