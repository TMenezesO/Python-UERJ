import numpy as np
import matplotlib.pyplot as plt


## Definicoes das funcoes para o problema

def matrizT(matriz): ## List comprehension
   result = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
   return result

def matrizT_numpy(matriz): ## modulo numpy
    
    #print(matriz) 
    #print("\n") 
    #print(np.transpose(matriz))
    return np.transpose(matriz)
   
def histo(lista,xlabel): ## histogramas
   plt.xlabel(xlabel)
   plt.hist(lista)
   plt.show()
   
def openfile(nome_arquivo): ## abrir o arquivo
   arquivo = open(nome_arquivo,'r')
   linhas = arquivo.readlines()
   return arquivo,linhas

#######################################################################
#######################################################################

A=[]
dicionario={}
diciNome={}


f,linhas = openfile("dados_alunos.txt")

for line in linhas:
    #aqui vamos obter os dados linha por linha, quer dizer idade altura e peso aluno por aluno
    dados = line.split()
    #print(len(dados),dados[0],type(dados[0]))
    fdados = [float(x) for x in dados]
   # print(len(fdados),fdados[0],type(fdados[0]))
    A.append(fdados)
    

AT = matrizT(A)
#AT = matrizT_numpy(A)

for i in range(0,len(AT)):
   dicionario[i] = AT[i]


nome_coluna=["idade","altura","massa"]
for i  in  range (0,len(AT)):
   diciNome[nome_coluna[i]] = AT[i]



histo(diciNome["idade"],"idade (anos)")   
histo(diciNome["altura"],"altura (m)")
histo(diciNome["massa"],"massa (kg)")