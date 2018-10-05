#from math import *
#import math as <nome>
import math

def angulo(co,ca):
   tan=co/ca
   theta=math.atan(tan)
   #theta_graus=theta*180/math.pi
   #print (theta_graus)
   print(math.degrees(theta),"graus")
   print(theta,"radianos")

angulo(4,2)

def angulo2(theta):
   y=math.degrees(math.acos(theta))
   print (y,"graus")

angulo2(math.sqrt(2)/2)

