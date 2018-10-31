import math
#25 intervalos de 1 min
def ex1(do,dt,v):
    lista_d=[]
    lista_d.append(do)
    d=do
    for i in range(int((dt/v)*60)):
        d=d + v*(1/60)
        lista_d.append(d)
    print (lista_d)
    return lista_d

#ex1(0,5,12)

#O/A mesmo/a atleta no seguinte trecho acelera por $200$ metros até chegar em $15 km/h$ por $2 km$.
#Queremos obter uma tabela ou gráfico da distância percorrida en função do tempo e o tempo total para chegar em $7 km$,
#faça isto utilizando listas.
#d=0.2
#vo=12
#v=15
#v = vo + at
#a= (v-vo)/t
#v*v = vo*vo + 2*a*d

def acc(v,vo,d):
    a = ((math.pow(v,2) - math.pow(vo,2))/2*d)
    print (a)
    return a

#acc(15,12,0.2)

def vel(vo,v):
    a=acc(15,12,0.2)
    lista_v=[]
    lista_v.append(vo)
    v=vo
    for i in range():
        v = v + a*(1/60)
        d=d + v*(1/60)
        lista_v.append(v)
        lista_d.append(d)
    print (lista_v)
    return lista_v
vel(12,15)
#ex1(0,5,12)