
#Utilizando dicionários, escreva uma função que tome como argumento uma palavra (string) e 
#retorne um dicionário que tem como key a letra da palavra e como valor o número de vezes que
#ela aparece na palavra. Tal dicionário é chamado de tabela de frequência. 
#Dica: Utilize o método get dos dicionários.
#dict = {key:value}

def contagem_de_letras(string):
    dict_palavra = {}
    palavra = str(string)
    for i in palavra:
        dict_palavra = {i:'oi'}
        #i = dict_palavra.keys()
        #print(dict_palavra.keys())
        #dict_palavra.keys() = i
        print(dict_palavra)
    return dict_palavra

contagem_de_letras("tr")



#def newcounter(n):
#    count = 0
#    str_numero=str(n)
#    for i in str_numero:
#        if i=='0' or i=='5':
#            count = count + 1
#    print (count)
#    return count

#for x in list_ex2:
#    newcounter(x)