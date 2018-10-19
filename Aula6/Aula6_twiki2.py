import turtle
import math
sammy = turtle.Turtle()
jn = turtle.Screen()         
jn.bgcolor("white")

#cores = ["yellow", "orange", "purple", "lightblue","violet","white"]


def estrela(x,color):
    for i in range(x):
        sammy.color(color)
        sammy.speed(0)
        sammy.pensize(3)
        sammy.left((180-((180*(x-2))/x))*2)
        sammy.forward(50)

#    ((x - 2)*180/x)
       
    jn.mainloop()

estrela(23,"red")