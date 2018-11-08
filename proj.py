import math
import turtle
import matplotlib.pyplot as plt

def pend(k,m,lo,r):
    x=0
    #x=lo*math.cos(theta)
    z=0
    #x=lo*math.sin(theta)
    vx=0
    vz=0
    
    lista_vx=[]
    lista_vz=[]
            
    lista_x=[]
    lista_z=[]
            
    lista_ax=[]
    lista_az=[]

    for i in range(0,180,1):
        theta=i
        x=lo*math.cos(theta)
        z=lo*math.sin(theta)
        for n in range(0,60,1):
            t=n
            g=9.81
            ax = -(k/m)*(r-lo)*math.sin(theta)
            az= -g + (k/m)*(r-lo)*math.cos(theta)
            
            lista_ax.append(ax)
            lista_az.append(az)
            
            
            
        #vx[n] = vx[n-1] + ax[n-1]*t
        #vz[n] = vx[n-1] + az[n-1]*t
        #x[n] = x[n-1] + vx[n-1]*t
        #z[n] = z[n-1] + vz[n-1]*t
        
            vx = vx + ax*t
            vz = vz + az*t
            lista_vx.append(vx)
            lista_vz.append(vz)
            
            v = math.sqrt(math.pow(vx,2) + math.pow(vz,2))
            
            d = math.sqrt(math.pow(x,2) + math.pow(z,2))
            
            
            x = x + vx*t
            z = z + vz*t
            
            lista_x.append(x)
            lista_z.append(z)
            
            print(lista_ax)
            print(lista_az)
            
    plt.plot(t,x)
    plt.xlabel("tempo s")
    plt.ylabel("distancia m")
    
    plt.plot(t,z)
    plt.xlabel("tempo s")
    plt.ylabel("distancia m")
            
            #print(lista_vx)
            #print(lista_vz)
            #print(lista_x)
            #print(lista_z)

pend(1,1,1,2)    
       