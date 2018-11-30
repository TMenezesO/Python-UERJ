#1) Escreva uma função chamada ler_arquivos que tome como argumento um nome de arquivo, 
#leia um arquivo com um número qualquer de colunas e retorne um dicionário que tenha como keys os números das colunas e como valor 
#uma lista dos valores associados a cada coluna do arquivo. Use o arquivo dados_alunos.txt. 
# Caso o arquivo tiver o cabeçalho das colunas, p.ex. dados_alunos_com_cabecalho.txt, o key deve ser a palavra do cabeçalho.

def ler_arquivo(nome_arquivo):
    dict_values={}
    f = open(nome_arquivo,'r')
    linhas = f.readlines()
    for line in linhas:
        for i in range(len(line.split())):
            dict_values[i]=[]
    for line in linhas:
        for i in range(len(line.split())):
            dict_values[i].append(line.split()[i])
    print(dict_values)
    return dict_values
        
#
#ler_arquivo("dados_alunos.txt")


def ler_arquivo_new(nome_arquivo):
    dict_values={}
    f = open(nome_arquivo,'r')
    colunas = f.readline()
    linhas = f.readlines()
    #linha = [f.readline(0)]
    #print(colunas.split())
    for line in linhas:
        for i in range(len(line.split())):
            dict_values[colunas.split()[i]]=[] ###
    for line in linhas:
        for i in range(len(line.split())):
            dict_values[colunas.split()[i]].append(line.split()[i]) ####
    print(dict_values)
    return dict_values


ler_arquivo_new("dados_alunos_com_cabecalho.txt")
