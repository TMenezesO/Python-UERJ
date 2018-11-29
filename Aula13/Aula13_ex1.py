#Utilizando um arquivo de dados com varias colunas (por exemplo, o arquivo dados_alunos.txt), 
#faca um histograma com os dados de cada uma das colunas. 
#Dica: utilize o matplotlib para fazer os histogramas.
import matplotlib.pyplot as plt


fout = open('dados_alunos.txt', 'r')
linhas = fout.readlines()

lista_idade=[]
lista_altura=[]
lista_peso=[]

for line in linhas:
    column = line.strip().split('\t')
    lista_idade.append(float(line.split()[0]))
    lista_altura.append(float(line.split()[1]))
    lista_peso.append(float(line.split()[2]))
fout.close()
#print(lista_idade)   
#print(lista_altura)
#print(lista_peso)

def histo(lista):
    plt.hist(lista)
    plt.show()

histo(lista_idade)   
histo(lista_altura)
histo(lista_peso)
