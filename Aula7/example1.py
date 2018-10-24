
import math

list_valores=[1,2,3,4,5,6,100,256,10000] # lista de valores para as duas primeiras funções
list_sqrt=[-25,-16,-9,0,9,64,89,200,4096] # lista de valores para o exemplo da sqrt

def par_impar(x):
    if x % 2 == 0:
        print(x, " é par.")
        print("Você sabia que 2 é o único número par que é também número primo?")
    else:
        print(x, " é impar.")
        print("Você sabia que a multiplicação de dois números ímpares " + "sempre gera um resultado ímpar?")

def declaracao_cond(x):

    if x < 0:
        print("O número negativo ",  x, " não é válido.")
        #x = 42
        print("Decidi usar o número 42.")

    print("A raiz quadrada de ", x, "é", math.sqrt(x))
    

def print_raiz_quadrada(x):
    if x <= 0:
        print("Somente valores positivos, por favor.")
        return
    else:
        result = x**0.5
        print("A raiz de ", x, "é", result)
    #elif x > 0 and x < 25
        #result = x**0.5
        #print("A raiz de ", x, "é", result)
    #else:
    #    print('a')
    
for i in list_valores:
    
    par_impar(i)
    declaracao_cond(i)
    
for y in list_sqrt:
    print_raiz_quadrada(y)
