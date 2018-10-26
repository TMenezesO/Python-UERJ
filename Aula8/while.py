
def soma_ate(n,debug):
    """ Retorna a soma de 1+2+3 ... n """
    ss  = 0
    v = 1
    while v <= n:      
        ss = ss + v
        #if debug: print (ss)
        v = v + 1
        if debug: print (v)
    return ss

print(soma_ate(8,True))