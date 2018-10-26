lista_valores=[29,23,45,50,26,44]
#debug=True or False

def Collatz(n,debug):
    while n > 1:
        if n % 2 == 0:
            n = n/2
            if debug: print (n)
        else:
            n = 3*n + 1
            if debug: print (n)
    print (n,"\n")
    
for valor in lista_valores:
    Collatz(valor,True)