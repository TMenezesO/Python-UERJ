import math
#list_n=[1,2,3,4,5,6,7]

def factorial(x):
   y=math.factorial(x)
   print (x,"!=",y)
   return y

for x in range(100):
#for x in list_n:
   #if x >= 1:
   factorial(x)
