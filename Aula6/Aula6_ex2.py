import turtle
jn = turtle.Screen()         # Configurar a janela e seus atributos
jn.title("Mob e Sam")

mob = turtle.Turtle()       # Criar e configurar alguns atributos de 
sam = turtle.Turtle()

cor=input("Digite uma cor para o fundo: ")

jn.bgcolor(cor)

mobcolor=input("Cor Mob: ")
samcolor=input("Cor Sam: ")

mob.color(mobcolor)
sam.color(samcolor)

mobpensize=input("pensize mob: ")
sampensize=input("pensize sam: ")



mob.pensize(int(mobpensize))
sam.pensize(int(sampensize))  

mob.forward(80)             # Fazer mob desenhar um triângulo equilátero
mob.left(120)
mob.forward(80)
mob.left(120)
mob.forward(80)
mob.left(120)               # Completar o triângulo

mob.right(180)              # Fazer mob dar meia volta
mob.forward(80)             # Movê-la para longe da origem

mob.color("red")
mob.pensize(4)

sam.forward(50)             # Fazer sam desenhar um quadrado
sam.left(90)
sam.forward(50)
sam.left(90)
sam.forward(50)
sam.left(90)
sam.forward(50)
sam.left(90)

sam.color("lightblue")
sam.pensize(4)
#jn.mainloop()
