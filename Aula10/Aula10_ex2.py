#2) Crie uma lista com números sequenciais com incrementos de uma unidade, de 1 até 10000. Dica: use a função range.

def onetoten():
    lista=[]
    for i in range(1,10001,1):
        lista.append(i)
        
    print (lista)
    return lista

onetoten()