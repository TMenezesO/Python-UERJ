import turtle
sammy = turtle.Turtle()
jn = turtle.Screen()         #
jn.bgcolor("black")

cores = ["yellow", "orange", "purple", "lightblue","violet","white"]

## quadrado

#for i in [0,1,2,3,4]:
for i in range(5):
    sammy.pensize(3)
    sammy.color(cores[i])
    sammy.forward(250)
    sammy.left(144)
    
