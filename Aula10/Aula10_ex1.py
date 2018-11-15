def dobrar_elementos(uma_lista):
    """ Reescreve os elementos de uma_lista com o dobro de seus valores originais.
    """
    for (i, valor) in enumerate(uma_lista):
        novo_elem = 2 * valor
        uma_lista[i] = novo_elem

    return uma_lista

#minha_lista = [2, 4, 6]
#print(minha_lista)
#dobrar_elementos(minha_lista)
#print(minha_lista)

#a) Modifique a função para retornar uma nova lista, sem modificar a lista usada como parâmetro. Esse tipo de função é chamado de função pura.
#b) Modifique a documentação de ajuda da nova função, de tal forma que quando se chame a função help da nova função, se obtenha a descrição adequada.

def nomod(lista):
    """ Transcreve os elementos da lista para outra lista, sem alterá-los
    """
    for (i,j) in enumerate(lista):
        novo = j
        lista[i] = novo
    
    print (lista)
    return lista


lista = [1,2,3,4]

nomod(lista)
help(nomod)
#print(lista)