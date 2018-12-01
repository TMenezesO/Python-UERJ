#Escreva um script que importe o módulo criado acima e faça um histograma para cada coluna do arquivo, com seus respectivos valores. Use o dicionário criado em 1).

import matplotlib.pyplot as plt
from Aula14_ex1 import *

def histo(lista):
    plt.hist(lista)
    plt.show()
    
d = ler_arquivo("dados_alunos.txt")

lista = d[0]
print(lista)

histo(d[0])
histo(d[1])
histo(d[2])

#print (d)