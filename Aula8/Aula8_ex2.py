def counter(n):
    count = 0
    while n!=0:
        count = count + 1
        n = n // 10         # divisão de inteiros
    print (count)
    return count

list_ex2=[10568,50505,50000,12346]


def newcounter(n):
    count = 0
    str_numero=str(n)
    for i in str_numero:
        if i=='0' or i=='5':
            count = count + 1
    print (count)
    return count

for x in list_ex2:
    newcounter(x)