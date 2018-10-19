import turtle
sammy = turtle.Turtle()
jn = turtle.Screen()         
jn.bgcolor("white")

#cores = ["yellow", "orange", "purple", "lightblue","violet","white"]

def estrela():
    for i in range(5):
        sammy.pensize(3)
 #       sammy.color(cores[i])
        sammy.left(144)
        sammy.forward(250)
       
    jn.mainloop()

estrela()