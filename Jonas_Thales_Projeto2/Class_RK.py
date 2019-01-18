#Alunos - Jonas Silva de Paiva e Thales Menezes de Oliveira
#Disciplina - Introducao a Python
#Profs -  Clemencia Mora & Helena Malbouisson
#Data - 18/01/2019
#Projeto 2: Colisoes Relativisticas - Aniquilacao eletron-positron - Classe e Metodos


import numpy
import math
import random
import matplotlib.pyplot as plt

# Classe para os 4-vetores

class FourVector:
    def __init__(self, E = 0, px = 0, py = 0, pz = 0, p = None):
        self.E = E
        self.px = px
        self.py = py
        self.pz = pz
    
    def momentum(self):
        p = math.sqrt(self.px*self.px + self.py*self.py + self.pz*self.pz)
        return p

    def invariant_mass_for_ee(self,other):
        m = math.sqrt(self.m*self.m + other.m*other.m + 2*self.m*other.E)
        return m
    
    def invariant_mass_for_yy(self,other,theta):
        m = math.sqrt((2*self.E*other.E)*(1 - math.cos(theta)))
        return m
    
        
class Photon(FourVector):
    def __init__(self, E = 0, px = 0, py = 0, pz = 0,):
        FourVector.__init__(self, E = 0, px = 0, py = 0, pz = 0)
        

class Lepton(FourVector):
    def __init__(self, E = 0, px = 0, py = 0, pz = 0, m = 0.511):
        FourVector.__init__(self)    
        self.E = E
        self.px = px
        self.py = py
        self.pz = pz
        self.m = 0.511
        

def plot_plt(x,y,xlabel,ylabel):
    # A funcao toma como argumentos duas listas, que serao os dados do histograma, e as duas strings referentes aos nomes dos eixos
    plt.scatter(x,y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
#    plt.close()


