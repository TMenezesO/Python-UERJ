import math
import matplotlib.pyplot as plt

#25 intervalos de 1 min

def acc(v,vo,d):
    a = ((math.pow(v,2) - math.pow(vo,2)))/(2*(0.2))
    print (a)
    return a

def ex1(do,dt,v):
    lista_d=[]
    lista_d.append(do)
    d=do
    for i in range(int((dt/v)*60)):
        d=d + v*(1/60)
        lista_d.append(d)
    print (lista_d)
    return lista_d

def vel1(vo,v,d):
    a=acc(15,12,0.2)
    lista_v=[]
    lista_v.append(vo)
    d=vo
    while v < 15:
        for i in range(int((v-vo/a)*60)):
            v = v + a*(1/60)
            lista_v.append(v)
    print (lista_v)
    return lista_v

vel1(12,15,0.2)
#ex1(0,5,12)

#O/A mesmo/a atleta no seguinte trecho acelera por $200$ metros até chegar em $15 km/h$ por $2 km$.
#Queremos obter uma tabela ou gráfico da distância percorrida en função do tempo e o tempo total para chegar em $7 km$,
#faça isto utilizando listas.
def acc(v,vo,d):
    a = ((math.pow(v,2) - math.pow(vo,2)))/(2*(0.2))
    print (a)
    return a

#acc(15/3.6,12/3.6,200)
#a=acc(15,12,0.2)

t = (15-12)/a
print (t*60)

def vel(vo,v,do):
    a=acc(15,12,0.2)
    lista_v=[]
    lista_d=[]
    lista_t=[]
    lista_d.append(do)
    lista_v.append(vo)
    v=vo
    d=do
    dt=12
    vt=5
    #while v < 15.0 and d < 7.0:
    for i in range(int(((v-vo)/a)*60)):
    #for i in range(22):
        #print (int(((v-vo)/a)*60))
        v = v + a*(1/60)
        d=d + v*(1/60)
        lista_v.append(v)
        lista_d.append(d)
        lista_t.append((d/v)*60)
        
        
    #plt.plot(d,d/v)
    #plt.xlabel("tempo s")
    #plt.ylabel("distância m")
    #print (lista_v)
    #print (lista_d)
    #print (lista_t)
    return lista_v
#vel(12,15,5)
#ex1(0,5,12)