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
    plt.savefig("file.png")


def pend_mola(xo,zo,k,m,lo):
    
## Definicao das condicoes iniciais do problema
## Para o caso do pendulo com mola, as posicoes iniciais (xo,zo) devem ser diferentes de 0
    x=xo
    z=zo
    vx=0
    vz=0
    
## Criacao das listas para aceleracao, velocidade e posicao    
    
    lista_vx=[]
    lista_vz=[]
            
    lista_x=[]
    lista_z=[]
            
    lista_ax=[]
    lista_az=[]
    
    lista_a=[]
    lista_v=[]
    lista_r=[]
    
    
    
    t1 = [i/100 for i in range(0,1000)]
    dt = t1[1] - t1[0]

    for t in t1:
        
        #ax = -(k/m)*(r-lo)*math.sin(theta) + (math.pow(v,2)/r)
        #az = -g -(k/m)*(r-lo)*math.cos(theta) + (math.pow(v,2)/r)
        
        #ax = -(k/m)*((math.sqrt(math.pow(x,2) + math.pow(z,2)))-lo)*(x/(math.sqrt(math.pow(x,2) + math.pow(z,2)))) + (math.pow(vx,2) + math.pow(vz,2))/math.sqrt(math.pow(x,2) + math.pow(z,2))
        #az = -g -(k/m)*((math.sqrt(math.pow(x,2) + math.pow(z,2)))-lo)*(z/(math.sqrt(math.pow(x,2) + math.pow(z,2)))) + ((math.pow(vx,2) + math.pow(vz,2))/math.sqrt(math.pow(x,2) + math.pow(z,2)))
        
        ax = -(k/m)*((math.sqrt(math.pow(x,2) + math.pow(z,2)))-lo)*(x/(math.sqrt(math.pow(x,2) + math.pow(z,2)))) + (math.pow(vx,2))/(math.sqrt(math.pow(x,2) + math.pow(z,2)))
        az = -g -(k/m)*((math.sqrt(math.pow(x,2) + math.pow(z,2)))-lo)*(z/(math.sqrt(math.pow(x,2) + math.pow(z,2)))) + (math.pow(vz,2))/(math.sqrt(math.pow(x,2) + math.pow(z,2)))
        
        
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
            
        a = math.sqrt(math.pow(ax,2) + math.pow(az,2))
        v = math.sqrt(math.pow(vx,2) + math.pow(vz,2))
        r = math.sqrt(math.pow(x,2) + math.pow(z,2))
        
        lista_a.append(a)
        lista_v.append(v)
        lista_r.append(r)
        
    
## arquivos de saida com as informacoes de aceleracao, velocidade e distancia, para as coordenas x e z e os valores em modulo
        
        zip(lista_a,lista_v,lista_r)
    with open('acc_vel_dist_mola.txt', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(zip(lista_a,lista_v,lista_r))
        
        zip(lista_ax,lista_vx,lista_x)
    with open('acc_vel_dist_x_mola.txt', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(zip(lista_ax,lista_vx,lista_x))
        
        zip(lista_az,lista_vz,lista_z)
    with open('acc_vel_dist_z_mola.txt', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(zip(lista_az,lista_vz,lista_z))

            
        #print(lista_vx)
        #print(lista_vz)

## Criacao dos histogramas |v| vs.t, |r| vs.t, |a| vs.t, vx vs. x, vz vs. z

    plot_plt(t1,lista_r,"tempo (s)","distancia (m)")
    plot_plt(t1,lista_v,"tempo (s)","velocidade (m/s)")
    plot_plt(t1,lista_a,"tempo (s)","aceleracao (m/s^2)")
    plot_plt(lista_x,lista_vx,"x (m)","vx (m/s)")
    plot_plt(lista_z,lista_vz,"z (m)","vx (m/s)")
    
  
                
#pend_mola(1,1,1,1,1)


def pend_simples(xo,zo):
    g=9.81
    x=xo
    z=zo
    vx=0
    vz=0
    
    lista_vx=[]
    lista_vz=[]
            
    lista_x=[]
    lista_z=[]
            
    lista_ax=[]
    lista_az=[]
    
    lista_a=[]
    lista_v=[]
    lista_r=[]



    t1 = [i/10 for i in range(0,100)]
    dt = t1[1] - t1[0]

    for t in t1:

        #ax = -g*(math.fabs(z)/(math.sqrt(math.pow(x,2) + math.pow(z,2))))*(x/(math.sqrt(math.pow(x,2) + math.pow(z,2)))) + (math.pow(vx,2) + math.pow(vz,2))/(math.sqrt(math.pow(x,2) + math.pow(z,2)))
        #ax = (-g*(math.fabs(z)*x))/(math.pow(x,2) + math.pow(z,2))
        #az = -g + g*math.pow((math.fabs(z)/(math.sqrt(math.pow(x,2) + math.pow(z,2)))),2) + (math.pow(vx,2) + math.pow(vz,2))/(math.sqrt(math.pow(x,2) + math.pow(z,2)))
    
        ax = -g*(math.fabs(z)/(math.sqrt(math.pow(x,2) + math.pow(z,2))))*(x/(math.sqrt(math.pow(x,2) + math.pow(z,2)))) + math.pow(vx,2)/(math.sqrt(math.pow(x,2) + math.pow(z,2)))
        az = -g + g*math.pow((math.fabs(z)/(math.sqrt(math.pow(x,2) + math.pow(z,2)))),2) + math.pow(vz,2)/(math.sqrt(math.pow(x,2) + math.pow(z,2)))
    
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
        
        a = math.sqrt(math.pow(ax,2) + math.pow(az,2))
        v = math.sqrt(math.pow(vx,2) + math.pow(vz,2))
        r = math.sqrt(math.pow(x,2) + math.pow(z,2))
        
        lista_a.append(a)
        lista_v.append(v)
        lista_r.append(r)
        
        zip(lista_a,lista_v,lista_r)
    with open('acc_vel_dist_simples.txt', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(zip(lista_a,lista_v,lista_r))
        
        zip(lista_ax,lista_vx,lista_x)
    with open('acc_vel_dist_x_simples.txt', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(zip(lista_ax,lista_vx,lista_x))
        
        zip(lista_az,lista_vz,lista_z)
    with open('acc_vel_dist_z_simples.txt', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(zip(lista_az,lista_vz,lista_z))


    plot_plt(t1,lista_r,"tempo (s)","distancia (m)")
    plot_plt(t1,lista_v,"tempo (s)","velocidade (m/s)")
    plot_plt(t1,lista_a,"tempo (s)","aceleracao (m/s^2)")
    plot_plt(lista_x,lista_vx,"x (m)","vx (m/s)")
    plot_plt(lista_z,lista_vz,"z (m)","vx (m/s)")
    
pend_simples(10,10)
