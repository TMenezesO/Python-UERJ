
#Utilizando dicionários, escreva uma função que tome como argumento uma palavra (string) e 
#retorne um dicionário que tem como key a letra da palavra e como valor o número de vezes que
#ela aparece na palavra. Tal dicionário é chamado de tabela de frequência. 
#Dica: Utilize o método get dos dicionários.
#dict = {key:value}

def contagem_de_letras(string):
    dict_palavra = {}
    palavra = str(string)
    for i in palavra:
        dict_palavra[i] = dict_palavra.get(i,0) + 1
        #dict_palavra[i] = palavra.count(i)
    print(dict_palavra)
    for l in sorted(dict_palavra):
        print(l + str(dict_palavra[l]))
    
    
    return dict_palavra

contagem_de_letras("equztreuqzqwteuqweindasjwuidhausihduaisusiad")
