import turtle
def draw_bar(t, height,color):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()           # Added this line
    t.left(90)
    t.forward(height)
    t.write("  "+ str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()             # Added this line
    #t.forward(10)

    wn = turtle.Screen()         # Set up the window and its attributes
    wn.bgcolor("lightgreen")

tess = turtle.Turtle()       # Create tess and set some attributes
#tess.color("blue", "red")
tess.pensize(3)



#xs = [48,117,200,240,160,260,220]
xs=[]
list_colors=[]
def fst():
    #xs=[]
    bins=input("Digite o n de bins: ")
    for i in range(int(bins)):
        xs.append(input("Digite um valor: "))
    for i in range(int(bins)):
        list_colors.append(input("Digite uma cor: "))
    print (xs)
    print (list_colors)

    #return xs
fst()

#for i in list_colors:
#    tess.color(i,i+1)



for a in xs:
    for color in list_colors:
        draw_bar(t, int(a), color)


wn.mainloop()