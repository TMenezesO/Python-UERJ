#Adapte a função acima para, se ocorrer um erro ao abrir, ler ou fechar arquivos, o programa capturar a exceção, imprimir uma mensagem de erro e sair.




def ler_arquivo(nome_arquivo):
    dict_values={}
    try:    
        f = open(nome_arquivo,'r')
        linhas = f.readlines()
        for line in linhas:
            for i in range(len(line.split())):
                dict_values[i]=[]
        for line in linhas:
            for i in range(len(line.split())):
                dict_values[i].append(line.split()[i])
        print(dict_values)
    except:
        print('Algo de errado aconteceu.')
    
    return dict_values
        


#
#ler_arquivo("dados_alunos.txt")

def ler_arquivo_new(nome_arquivo):
    try:   
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
    except:
        print('Algo de errado aconteceu.')
    
    return dict_values


ler_arquivo_new("dados_alunos_com_cabecalho.txt")