#3) Escreva uma função que, dado um número n, encontre o primeiro inteiro positivo entre 101 e menor que n, que seja divisível por 21. Dica: use a função range.


def new(n):
    for i in range(101,n,1):
        if i % 21 == 0 and 101 < i < n:
            print (i)
            break
        

new(110)