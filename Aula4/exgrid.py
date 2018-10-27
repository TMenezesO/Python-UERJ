#def do_four(f,x):
#   do_twice(f,x)
#   do_twice(f,x)
   #f(print_twice,x)
   #f(print_twice,x)

#do_twice(print_twice,'uerj')
#do_four(print_twice,'uerj')

def new_do_twice(f):
   f()
   f()
   
def new_do_four(f):
   new_do_twice(f)
   new_do_twice(f)
   
   
def horiz_line():
   print("+ - - - -"),
   
def vert_line():
   print ("|       "),

def horizs_lines():
   new_do_twice(horiz_line)
   # A ideia aqui é fazer + - - - - + - - - - +
   print ("+")

def verts_lines():
   new_do_twice(vert_line)
   print ("|")
   
def rows():
   new_do_twice(horizs_lines)
   new_do_four(verts_lines)
   
def hepgrid():
   new_do_twice(rows)
   horizs_lines()
   

#rows()
hepgrid()

#horizs_lines()
