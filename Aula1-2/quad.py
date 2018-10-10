import math
debug=True
def quad(a,b,c,debug):
    delta=math.sqrt(b*b - 4*a*c)
    if debug:
        print (type(delta),type(a),type(b),type(c))
        print (delta*delta)
    x1= (-b + delta)/(2*a)
    x2= (-b - delta)/(2*a)
    print (x1),(x2),type(x1),type(x2)
    
    
quad(3,-4,-10,debug)

    
    
