

def MRU(xi,xf,t,debug):
   if debug:
      print("xi =",xi,"xf =",xf,"t =",t)
   vmedia=(xf-xi)/t
   print("Velocidade Média =",vmedia)

def MRUA(a,t,debug):
   if debug:
      print("a =",a,"t =",t)
   v=a*t
   print("Velocidade =",v)

MRU(0,100,10,True)
MRUA(9.81,5,True)

