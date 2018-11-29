matrix = {(0, 0): 0, (0, 1): 0, (0, 2): 0, (0,3): 1, (0,4): 0, (1, 0): 0, (1, 1): 0, (1, 2): 0, (1,3): 0, (1,4): 0,
    (2, 0): 0, (2, 1): 2, (2, 2): 0, (2,3): 1, (2,4): 0, (3, 0): 0, (3, 1): 0, (3, 2): 0, (3,3): 0, (3,4):0,
    (4, 0): 0, (4, 1): 0, (4, 2): 0, (4,3): 3, (4,4): 0}

print(matrix.get((0,3)))
print(matrix.get((2,1)))
print(matrix.get((4,3)))
print(matrix.get((2,2)))



#matrix.get((2,2))
#(0,3), (2,1), (4,3) e (2,2). 


#print(matrix)







def matrixctr():
    matrix={}
    for i in range(0,5):
        for j in range(0,5):
            if j == 3:
                matrix = {(i, j):1}
            else:
                matrix = {(i, j):0}
        #print(matrix)
        #return matrix
        for j in range(0,5):
            matrix = {(i, j):0}
        #print(matrix)
        print(matrix)
    return matrix
    print(matrix.get((0,0)))

#matrixctr()


        
def secline():
    for i in range(0,5):
        matrix = {(1, i):0}
        print(matrix)
    return matrix

def thirdline():
    for i in range(0,5):
        if i == 1:
            matrix = {(2,i):2}
        else:
            matrix = {(2,i):0}
        print(matrix)
    return matrix
    
    
def fourthline():
    for i in range(0,5):
        matrix = {(3, i):0}
        print(matrix)
    return matrix

def fifthline():
    for i in range(0,5):
        if i == 1:
            matrix = {(4,i):3}
        else:
            matrix = {(4,i):0}
        print(matrix)
    return matrix

"    """"for i in range(0,5):
        matrix = {(1, i):0}
    for i in range(0,5):
        if i == 1:
            matrix = {(2,i):2}
        else:
            matrix = {(2,i):0}
        """""

#firstline()
#secline()
#thirdline()
#fourthline()
#fifthline()

    
#print(matrix)