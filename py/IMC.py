import math
listm=[11]
listh=[0.7]
def IMC(m,h):
    imc=m/(h*h)
    print ("IMC",imc)
    
for m in listm:
    for h in listh:
        IMC(m,h)
        
listh=[3,5,6,7,8,10]
g=9.81
def vfinal(h):
    v=math.sqrt(2*g*h)
    print ("vfinal",v)
    t=h/v
    print ("tempo",t)
    
for ho in listh:
    vfinal(ho)
