import turtle
sammy = turtle.Turtle()
sammy.shape("turtle")
sammy.speed(10)
cores = ["yellow", "orange", "purple", "lightblue"]

jn = turtle.Screen()         # Configurar a janela e seus atributos
jn.title("Mob e Sam")


for i in range(4):
    sammy.pensize(3)
    sammy.color(cores[i])
    sammy.forward(250)
    sammy.left(90)
    
jn.mainloop()