import conversores
#from conversores import *

#tseg=horas_para_segs(4)
#dm=kms_para_metros(20)

tseg=conversores.horas_para_segs(4)
dm=conversores.kms_para_metros(20)

def vmedia(dm,tseg):
   vmed=dm/tseg
   print(vmed)
   return vmed
 
vmedia(dm,tseg)  
#vmed=dm/tseg
#print (vmed)
