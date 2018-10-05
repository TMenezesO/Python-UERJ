import math
from conversores import *

def mph2(t_min,d_milhas):
   d_km=d_milhas/1.610
   t_h=(t_min/60.0)
   vmed=d_km/t_h
   tmed=d_km/vmed   
   print (vmed,tmed)

mph2(30,4)



