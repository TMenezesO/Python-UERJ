import turtle
sammy = turtle.Turtle()
jn = turtle.Screen()         #
jn.bgcolor("black")

cores = ["yellow", "orange", "purple", "lightblue","violet","white"]


for i in range(4):
    for i in range(5):
        sammy.pensize(3)
        sammy.speed(4)
        sammy.shape("turtle")
        sammy.color(cores[i])
        sammy.forward(50)
        sammy.left(144)
  
    sammy.penup()
    sammy.forward(100)
    sammy.pendown()
    
jn.mainloop()