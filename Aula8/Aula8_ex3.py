lista1=[12,16,17,24,29]

def ex3(lista):
    for i in lista:
        if i % 2 == 1:
            break
        print(i)
    print("done")

# Generalizacao
ex3(lista1)

# Encapsulamento
ex3([12,16,17,24,29])




#for i in [12, 16, 17, 24, 29]:
#    if i % 2 == 1:  # If the number is odd
#       break        #  ... immediately exit the loop
#    print(i)
#print("done")