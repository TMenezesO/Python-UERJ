

def matriz():
    lista=[]
    for i in range(0,4,1):
        linha_da_matriz=[]
        for j in range(0,4,1):
            linha_da_matriz.append(0)
        lista.append(linha_da_matriz)
        
    lista[0][0] = -1
    lista[1][1] = 1
    lista[2][2] = 1
    lista[3][3] = 1
    print("matriz #eta" ,lista)
    print ("elemento 3x3" ,lista[3][3])
    return lista

matriz()





