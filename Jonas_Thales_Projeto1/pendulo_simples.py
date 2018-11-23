#Alunos - Jonas Silva de Paiva e Thales Menezes de Oliveira
#Disciplina - Introducao a Python
#Profs -  Clemencia Mora & Helena Malbouisson
#Data - 23/11/2018
#Projeto para o pendulo simples



import math
import turtle
import csv
import matplotlib.pyplot as plt
g=9.81

def plot_plt(x,y,xlabel,ylabel):
    # A funcao toma como argumentos duas listas, que serao os dados do histograma, e as duas strings referentes aos nomes dos eixos
    
    #plt.plot(x,y)
    plt.scatter(x,y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
    plt.close()
    
    
def calculo_modulo(x,z):
    # Obtencao do modulo de um vetor ,usando x e z como parametros 
    r = math.sqrt(math.pow(x,2) + math.pow(z,2))
    return r

def calculo_theta(x,z):
    #Obtencao do angulo para diferentes valores de x e z
    if (z <= 0):
        theta = math.atan(-x/z)
    elif (x <= 0 and z > 0): 
        theta = math.atan(z/x) - math.pi/2
    elif (x >= 0 and z > 0): 
        theta = math.pi/2 + math.atan(z/x)
    elif (x == 0 and z > 0):
        theta = math.pi
    return theta


def pendulo_simples(xo,zo):
    
    #Definicao das condicoes iniciais para  o usuario
    
   # m = float(input("Massa (kg): "))
   # lo = float(input("Comprimento natural da mola (m): "))  
   # xo = float(input("Posicao Inicial em x : "))
   # zo = float(input("Posicao Inicial em z : "))
    
    x=xo
    z=zo
    vx=0
    vz=0
    
    #Criacao das listas para aceleracao, velocidade e posicao para as duas coordenadas
    
    lista_vx=[]
    lista_vz=[]
            
    lista_x=[]
    lista_z=[]
            
    lista_ax=[]
    lista_az=[]
    
    lista_a=[]
    lista_v=[]
    lista_r=[]


# Definicao do intervalo de tempo 
    t1 = [i/1000 for i in range(0,10000)]
    dt = t1[1] - t1[0]

    for t in t1:
       
    # execucao da funcao que obtem os valores de r e theta para diferentes valores de x e z    
        r = calculo_modulo(x,z)
        theta = calculo_theta(x,z)

        #ax = g*math.cos(theta)*math.sin(theta) + ((math.pow(vx,2) + math.pow(vz,2))/(lo))*math.sin(theta)
        #az = -g +g*math.pow((math.cos(theta)),2) + ((math.pow(vx,2) + math.pow(vz,2))/(lo))*math.cos(theta)
        ## Consertar as acc
        ax = -g*math.cos(theta)*math.sin(theta) - ((math.pow(vx*math.cos(theta),2))/(r))
        az = -g +g*math.pow((math.cos(theta)),2) - ((math.pow(vz*math.sin(theta),2))/(r))
        
        vx = vx + ax*dt
        vz = vz + az*dt
        
        x = x + vx*dt
        z = z + vz*dt
            
        lista_ax.append(ax)
        lista_az.append(az)
            
        lista_vx.append(vx)
        lista_vz.append(vz)
        
        lista_x.append(x)
        lista_z.append(z)
        
        a = calculo_modulo(ax,az)
        v = calculo_modulo(vx,vz)
        r = calculo_modulo(x,z)   
          
        lista_a.append(a)
        lista_v.append(v)
        lista_r.append(r)
        
        
    ## criacao dos arquivos de saida com as informacoes de aceleracao, velocidade e distancia, para as coordenadas x e z (ax,vx,x e az,vz,z) 
    #e tambem para os valores em modulo (a,v,r)
    # Os arquivos em texto possuem as informacoes de intervalo de tempo, aceleracao, velocidade e distancia, nessa ordem, da esquerda para a direita
    
        zip(t1,lista_a,lista_v,lista_r)
    with open('acc_vel_dist_simples.txt', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(zip(t1,lista_a,lista_v,lista_r))
        
        zip(t1,lista_ax,lista_vx,lista_x)
    with open('acc_vel_dist_x_simples.txt', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(zip(t1,lista_ax,lista_vx,lista_x))
        
        zip(t1,lista_az,lista_vz,lista_z)
    with open('acc_vel_dist_z_simples.txt', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(zip(t1,lista_az,lista_vz,lista_z))
        
    
## Execucao da funcao para a criacao dos histogramas |v| vs.t, |r| vs.t, |a| vs.t, vx vs. x, vz vs. z
## Fornecendo as duas listas para os dois eixos, bem como o titulo dos eixos

    plot_plt(t1,lista_r,"tempo (s)","distancia (m)")
    plot_plt(t1,lista_v,"tempo (s)","velocidade (m/s)")
    plot_plt(t1,lista_a,"tempo (s)","aceleracao (m/s^2)")
    plot_plt(lista_x,lista_vx,"x (m)","vx (m/s)")
    plot_plt(lista_z,lista_vz,"z (m)","vx (m/s)")
    plot_plt(lista_x,lista_z,"x (m)","z (m)")
    
    
# Execucao da funcao para o pendulo simples 
pendulo_simples(.299,-2.99)
