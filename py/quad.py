import math
debug=True
def quad(a,b,c):
    delta=math.sqrt(b*b - 4*a*c)
    if debug:
        print delta*delta
    x1= (-b + delta)/(2*a)
    x2= (-b - delta)/(2*a)
    print x1,",",x2
    
    
quad(3,-4,-10)

    
    
