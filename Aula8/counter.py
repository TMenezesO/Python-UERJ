lc=[710,250,6500,80000,11000,43262]

def counter(n):
    count = 0
    while n!=0:
        count = count + 1
        n = n // 10         # divisão de inteiros
    print (count)
    return count

for x in lc:
    counter(x)