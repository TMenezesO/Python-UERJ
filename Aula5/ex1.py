list_values=[10,20,30]


def listoperations(lista):
	print (max(lista))
	print (min(lista))
	print (sum(lista))


def listmultiply(lista): 
    res = 1
    for x in lista: 
         res = res*x
    print (res)
    return res  
    


listoperations(list_values)
listmultiply(list_values)

