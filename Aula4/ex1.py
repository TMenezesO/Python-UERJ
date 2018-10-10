#def do_twice(f):
#   f ()  
#   f ()



#def print_spam (): 
#    print('spam') 

#do_twice (print_spam)

def print_twice(string):  
   print(string)
  

def do_twice(f,x):
   f(x)
   f(x)

#do_twice(print_twice,'uerj')


def do_four(f,x):
   do_twice(f,x)
   do_twice(f,x)
   #f(print_twice,x)
   #f(print_twice,x)

do_four(print_twice,'uerj')






