import math
import turtle
import csv
import matplotlib.pyplot as plt

g=9.81

def plot_plt(x,y,xlabel,ylabel):
    # A funcao toma como argumentos duas listas, que serao os dados do histograma, e as duas strings referentes aos nomes dos eixos
    
    plt.plot(x,y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


def pend_mola(xo,zo,k,m,lo):
    
## Definicao das condicoes iniciais do problema
    to=0
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
    lista_d=[]
    
    
    
    t1 = [i/100 for i in range(0,1000)]
    dt = t1[1] - t1[0]

    for t in t1:
        
        #r = (math.sqrt(math.pow(x,2) + math.pow(z,2)))
        #v = (math.sqrt(math.pow(vx,2) + math.pow(vz,2)))
        
        #ax = -(k/m)*(r-lo)*(x/r) + (v*v/r)
        #az = -g -(k/m)*(r-lo)*(z/r) + (v*v/r)
        
        #ax = -(k/m)*((math.sqrt(math.pow(x,2) + math.pow(z,2)))-lo)*(x/(math.sqrt(math.pow(x,2) + math.pow(z,2)))) + (math.pow(vx,2) + math.pow(vz,2))/math.sqrt(math.pow(x,2) + math.pow(z,2))
        #az = -g -(k/m)*((math.sqrt(math.pow(x,2) + math.pow(z,2)))-lo)*(z/(math.sqrt(math.pow(x,2) + math.pow(z,2)))) + ((math.sqrt(math.pow(vx,2) + math.pow(vz,2)))/math.sqrt(math.pow(x,2) + math.pow(z,2)))
        
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
        d = math.sqrt(math.pow(x,2) + math.pow(z,2))
        
        lista_a.append(a)
        lista_v.append(v)
        lista_d.append(d)
        
        zip(lista_a,lista_v,lista_d)
    with open('acc_vel_dist.txt', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(zip(lista_a,lista_v,lista_d))
        
        zip(lista_ax,lista_vx,lista_x)
    with open('acc_vel_dist_x.txt', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(zip(lista_ax,lista_vx,lista_x))
        
        zip(lista_az,lista_vz,lista_z)
    with open('acc_vel_dist_z.txt', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(zip(lista_az,lista_vz,lista_z))

            
        #print(lista_vx)
        #print(lista_vz)

    plot_plt(t1,lista_d,"tempo (s)","distancia (m)")
    plot_plt(t1,lista_v,"tempo (s)","velocidade (m/s)")
    plot_plt(t1,lista_a,"tempo (s)","aceleracao (m/s^2)")
    plot_plt(lista_vx,lista_x,"velocidade (m/s)","distancia (m)")
    plot_plt(lista_vz,lista_z,"velocidade (m/s)","distancia (m)")
    
  
                
pend_mola(1,1,1,1,1)


def pend_simples(xo,zo):
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
    lista_d=[]



    t1 = [i/100 for i in range(0,100)]
    dt = t1[1] - t1[0]

    for t in t1:

        ax = -g*(math.fabs(z)/(math.sqrt(math.pow(x,2) + math.pow(z,2))))*(x/(math.sqrt(math.pow(x,2) + math.pow(z,2)))) + (math.pow(vx,2) + math.pow(vz,2))/(math.sqrt(math.pow(x,2) + math.pow(z,2)))
        #ax = (-g*(math.fabs(z)*x))/(math.pow(x,2) + math.pow(z,2))
        az = -g + g*math.pow((math.fabs(z)/(math.sqrt(math.pow(x,2) + math.pow(z,2)))),2) + (math.pow(vx,2) + math.pow(vz,2))/(math.sqrt(math.pow(x,2) + math.pow(z,2)))

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
        
        zip(lista_a,lista_v,lista_d)
    with open('acc_vel_dist_simples.txt', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(zip(lista_a,lista_v,lista_d))
        
        zip(lista_ax,lista_vx,lista_x)
    with open('acc_vel_dist_x_simples.txt', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(zip(lista_ax,lista_vx,lista_x))
        
        zip(lista_az,lista_vz,lista_z)
    with open('acc_vel_dist_z_simples.txt', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(zip(lista_az,lista_vz,lista_z))


        a = math.sqrt(math.pow(ax,2) + math.pow(az,2))
        v = math.sqrt(math.pow(vx,2) + math.pow(vz,2))
        d = math.sqrt(math.pow(x,2) + math.pow(z,2))
        
        lista_a.append(a)
        lista_v.append(v)
        lista_d.append(d)
            
    plot_plt(t1,lista_d,"tempo (s)","distancia (m)")
    plot_plt(t1,lista_v,"tempo (s)","velocidade (m/s)")
    plot_plt(t1,lista_a,"tempo (s)","aceleracao (m/s^2)")
    plot_plt(lista_vx,lista_x,"velocidade (m/s)","distancia (m)")
    plot_plt(lista_vz,lista_z,"velocidade (m/s)","distancia (m)")
    
pend_simples(10,10)
