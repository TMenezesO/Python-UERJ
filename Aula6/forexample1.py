import turtle
sammy = turtle.Turtle()
jn = turtle.Screen()         #
jn.bgcolor("black")

cores = ["yellow", "orange", "purple", "lightblue"]

## quadrado

#for i in [0,1,2,3]:
for i in range(4):
    sammy.pensize(3)
    sammy.color(cores[i])
    sammy.forward(50)
    sammy.left(90)
    
## triângulo    
    
#for i in [0,1,2]:
#for i in range(3):
#    sammy.pensize(3)
#    sammy.color(cores[i])
#    sammy.forward(50)
#    sammy.left(120)