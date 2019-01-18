#Alunos - Jonas Silva de Paiva e Thales Menezes de Oliveira
#Disciplina - Introducao a Python
#Profs -  Clemencia Mora & Helena Malbouisson
#Data - 18/01/2019
#Projeto 2: Colisoes Relativisticas - Aniquilacao eletron-positron



import numpy
import math
import random
import matplotlib.pyplot as plt
from Class_RK import *
#from random import randrange, uniform

me = 0.511

# Criacao das listas para os histogramas do matplotlib
   
list_ph1_E = []
list_ph2_E = []   
list_theta = []

## Funcao para o a obtencao de k, e da energia do dois fotons
   
def el_pos_anh():
    

    k = math.sqrt((pos.E - ele.m)/(pos.E + ele.m))
    
    ph1.E = ele.m/(1 - k*math.cos(theta))
    ph2.E = (pos.E + ele.m - ph1.E)
    
    list_ph1_E.append(ph1.E)
    list_ph2_E.append(ph2.E)
    
    mee = FourVector.invariant_mass_for_ee(ele,pos)
    myy = FourVector.invariant_mass_for_yy(ph1,ph2,theta)
        
    return list_ph1_E,list_ph2_E,mee,myy

## ALguns valores para a energia Inicial do positron
list_Epos = [10,20,30,40,50,60]

##  Execucao do codigo para Epos, da lista, e theta aleatorio
for Epos in list_Epos:
    for i in range(1000): ## Quantidade de entradas 

        px_pos = random.uniform(1,10)
        py_pos = random.uniform(1,10)
        # pz_pos = random.uniform(1,10) Para 3D, caso seja necessario
        theta = random.uniform(0,6.28)

        
## Lista pra theta
        list_theta.append(theta)
    
            
#######  Estado Inicial  #######
        ele = Lepton(me,0,0,0,me)
        pos = Lepton(Epos,px_pos,py_pos,0,me)


####### Estado Final ########
        ph1 = Photon(0,0,0,0)
        ph2 = Photon(0,0,0,0)
    

 ### Execucao da funcao e listas para os plots 

        list_ph1_E,list_ph2_E,mee,myy = el_pos_anh()
        
## Massa invariante dos dois sistemas
        print(Epos,theta,"mee = ", mee,"myy = ",myy)
       #print("mee = ", mee,"myy = ",myy)

plot_plt(list_theta,list_ph1_E,"angulo theta","Energia_photon1")
plot_plt(list_theta,list_ph2_E,"angulo theta","Energia_photon2")