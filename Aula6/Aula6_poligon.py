import turtle
import math
sammy = turtle.Turtle()
jn = turtle.Screen()         
jn.bgcolor("white")

#cores = ["yellow", "orange", "purple", "lightblue","violet","white"]


def poligon(x,color):
    for i in range(x):
        sammy.color(color)
        sammy.speed(0)
        sammy.pensize(3)
 #      sammy.color(cores[i
        #sammy.left(180 - (180/x))
        sammy.left(180 - (((x - 2)*(180/x))))
        sammy.forward(10)
        #sammy.left(180 - (180/x))
        #sammy.left(180 - (math.pow((x+1),2)))
        
       
    jn.mainloop()

poligon(50,"red")