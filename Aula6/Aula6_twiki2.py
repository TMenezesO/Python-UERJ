mport turtle
import math

cores = ["yellow", "orange", "purple", "lightblue","violet","white"]

# DIferenças para estrelas com n de pontas pares ou ímpares

def estrela_impar(x,color): # funciona apenas para estrelas com n de pontas ímpar
    sammy = turtle.Turtle()
    jn = turtle.Screen()         
    jn.bgcolor("white")
    sammy.setpos((0,0))
# funciona apenas para número de pontas ímpar
    for i in range(x):
        sammy.color(color)
        sammy.speed(0)
        sammy.pensize(2)
        sammy.left(180.0 - (360.0/(2*x)))
        sammy.forward(250)

       
    jn.mainloop()
    
#estrela_impar(29,"red")

def estrela(n,cor):
    sammy = turtle.Turtle()
    jn = turtle.Screen()         
    jn.bgcolor("white")
    sammy.setpos((0,0))
    
    for i in range(n):
        if n % 2 == 0:
            sammy.color(cor)
            sammy.speed(0)
            sammy.pensize(2)
            sammy.left(180.0 - (360.0/(n)))
            sammy.forward(250)
    
        else:
            sammy.color(cor)
            sammy.speed(0)
            sammy.pensize(2)
            sammy.left(180.0 - (360.0/(2*n)))
            sammy.forward(250)
    
    jn.mainloop()
estrela(13,"green")
