#Alunos - Jonas Silva de Paiva e Thales Menezes de Oliveira
#Disciplina - Introducao a Python
#Profs -  Clemencia Mora & Helena Malbouisson
#Data - 18/01/2019
#Projeto 2: Colisoes Relativisticas - Aniquilacao eletron-positron



import numpy
import math
import random
import matplotlib.pyplot as plt
from RK_class import *
#from random import randrange, uniform


#Podem criar ou utilizar uma classe base de 4-vetor, e utilizar ela para construir suas
#particulas
#Criem um script que chame o modulo e definam uma funcao para resolver, dadas as
#condicoes iniciais :
#o angulo resultante das particulas finais na colisao
#o 4-momento das particulas do estado final
#a energia das particulas finais
#Com um gerador de numeros aleatorios, forneca a distribuicao de momento das partuculas iniciais para obter uma distribuicao de angulos/momentos e energia das
#particulas finais, e faca o grafico das distribuicoes. 

me = 0.511

# Criacao das listas para os histogramas do matplotlib
   
list_ph1_E = []
list_ph2_E = []   
list_theta = []

## Funcao para o a obtencao de k, e da energia do dois fotons
   
def el_pos_anh(pos_E,pos_px,pos_py,pos_m,ele_m):
    
    k = math.sqrt((pos_E - ele_m)/(pos_E + ele_m))
    
    ph1_E = ele_m/(1 - k*math.cos(theta))
    ph2_E = (pos_E + ele_m - ph1_E)
    
    ph1.E = ele_m/(1 - k*math.cos(theta))
    ph2.E = (pos_E + ele_m - ph1_E)
      
    list_ph1_E.append(ph1_E)
    list_ph2_E.append(ph2_E)
    
    mee = FourVector.invariant_mass_for_ee(ele,pos)
    myy = (FourVector.invariant_mass_for_yy(ph1,ph2))*math.sqrt((1 - math.cos(theta)))
    
    
    return list_ph1_E,list_ph2_E,mee,myy

Epos = 30
for i in range(1000):


    #Epos = random.uniform(1,1000)
    px_pos = random.uniform(1,1000)
    py_pos = random.uniform(1,1000)
    #pz_pos = random.uniform(1,10)
    theta = random.uniform(0,6.28)
    #theta = 0.0
    
## Lista pra theta
    list_theta.append(theta)
    
            
    #######  Estado Inicial  #######
    ele = Lepton(me,0,0,0,me)
    pos = Lepton(Epos,px_pos,py_pos,0,me)


####### Estado Final ########
    ph1 = Photon(0,0,0,0)
    ph2 = Photon(0,0,0,0)

### Execucao da funcao e listas para os plots 


    list_ph1_E,list_ph2_E,mee,myy = el_pos_anh(Epos,pos.px,pos.py,pos.m,ele.m)
    
## Massa invariante dos dois sistemas
    
    print("mee = ", mee,"myy = ",myy)

plot_plt(list_theta,list_ph1_E,"angulo theta","Energia_photon1")
plot_plt(list_theta,list_ph2_E,"angulo theta","Energia_photon2")