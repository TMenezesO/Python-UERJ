#Escreva um script que importe o módulo criado acima e faça um histograma para cada coluna do arquivo, com seus respectivos valores. Use o dicionário criado em 1).

import matplotlib.pyplot as plt
import statistics as stat
from Aula14_ex1 import *


def histo(lista):
    plt.hist(lista)
    plt.show()
    
def histo_new(lista,titulohist,titulox,tituloy):
    plt.hist(lista)
    plt.title(titulohist)
    plt.xlabel(titulox)
    plt.ylabel(tituloy)
    plt.show()
    
d= ler_arquivo("dados_alunos.txt")


for i in range(len(d)):
    histo(d[i])


histo_new(d[0],"Idade dos alunos","Idade (anos)","N de alunos")
histo_new(d[1],"IAltura dos alunos","Altura (m)","N de alunos")
histo_new(d[2],"Massa dos alunos","Massa (kg)","N de alunos")

lista_idade = [stat.mean(d[0]),stat.stdev(d[0]),stat.pstdev(d[0])]
lista_altura = [stat.mean(d[1]),stat.stdev(d[1]),stat.pstdev(d[2])]
lista_massa = [stat.mean(d[2]),stat.stdev(d[2]),stat.pstdev(d[2])]


print(lista_idade)
print(lista_altura)
print(lista_massa)

