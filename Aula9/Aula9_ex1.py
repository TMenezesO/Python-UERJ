
#25 intervalos de 1 min
def ex1(do,dt,v,debug):
    lista_d=[]
    lista_d.append(do)
    d=do
    for i in range(int((dt/v)*60)):
        d = d + v*(1/60)
        if debug: print(d)
        lista_d.append(d)
    print (lista_d)
    return lista_d

ex1(0,5,12,False)