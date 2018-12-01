#Escreva um programa que leia uma string e retorne uma tabela das letras do alfabeto em ordem alfabética que ocorrem na string junto com o número de vezes que cada letra ocorre.
#Letras maiúsculas devem deve ser ignoradas. Um exemplo de saída do programa quando o usuário digita os dados “ThiS is String with Upper and lower case Letters”, seria o seguinte:


def contagem_de_letras(string):
    dict_palavra = {}
    palavra = str(string)
    for i in palavra:
        #dict_palavra[i] = dict_palavra.get(i,0) + 1
        dict_palavra[i] = palavra.count(i)
    #print(dict_palavra)
        if i == "S" or i == "U" or i == "L":
            print("")
        else:
            for l in sorted(dict_palavra):
                print(l + ":" + str(dict_palavra[l]))
    
    
    return dict_palavra

contagem_de_letras("ThiS is String with Upper and lower case Letters”")
