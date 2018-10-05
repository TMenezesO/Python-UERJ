import math
import time

def angulozenital(lsombra,lobjeto):
   theta=math.atan(lsombra/lobjeto)
   print (theta)
   return theta
 

x = 10*(angulozenital(0.5,5))
print (x)


#print (time.localtime())
