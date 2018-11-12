import math
import turtle
import matplotlib.pyplot as plt

g=9.81

def pend_mola(xo,zo,k,m,lo,r):
    x=xo
    #x=lo*math.cos(theta)
    z=zo
    #x=lo*math.sin(theta)
    vx=0
    vz=0
    
    lista_vx=[]
    lista_vz=[]
            
    lista_x=[]
    lista_z=[]
            
    lista_ax=[]
    lista_az=[]

    for i in range(0,10,1):
        #for n in range(0,10,1):
        theta=i
        x=lo*math.cos(theta)
        z=lo*math.sin(theta)
        
        ax = -(k/m)*(r-lo)*math.sin(theta)
        az= -g + (k/m)*(r-lo)*math.cos(theta)
        for n in range(0,10,1):
            t=n
            #ax = -(k/m)*(r-lo)*math.sin(theta)
            #az= -g + (k/m)*(r-lo)*math.cos(theta)
            
            vx = vx + ax*t
            vz = vz + az*t
            
            x = x + vx*t
            z = z + vz*t
            
            lista_ax.append(ax)
            lista_az.append(az)

            lista_vx.append(vx)
            lista_vz.append(vz)
            
            lista_x.append(x)
            lista_z.append(z)
            
            a = math.sqrt(math.pow(ax,2) + math.pow(az,2))
            v = math.sqrt(math.pow(vx,2) + math.pow(vz,2))
            d = math.sqrt(math.pow(x,2) + math.pow(z,2))
            
            print(lista_x)
            print(lista_z)
            #print(math.cos(theta))
            #print((r-lo))
    plt.plot(t,d)
    plt.xlabel("tempo s")
    plt.ylabel("distancia m")
    
    plt.plot(t,v)
    plt.xlabel("tempo s")
    plt.ylabel("velocidade m/s")
    
    plt.plot(t,a)
    plt.xlabel("tempo s")
    plt.ylabel("aceleracao m/s^2")
    
    
    
    plt.plot(vx,x)
    plt.xlabel("velocidade m/s")
    plt.ylabel("distancia m")
    
    
    plt.plot(vz,z)
    plt.xlabel("velocidade m/s")
    plt.ylabel("distancia m")
    

    with open('your_file.txt', 'w') as f:
        for ax in lista_ax:
            for az in lista_az:
                f.write("%s\n" % ax)
                f.write("\t")
                f.write("%s\n" % az)
                
pend_mola(0,0,1,1,1,2)


def pend_simples():
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
            ax = -g*math.cos(theta)*math.sin(theta)
            az = -g + g*math.pow((math.cos(theta)),2)
            
            lista_ax.append(ax)
            lista_az.append(az)
        
            vx = vx + ax*t
            vz = vz + az*t
            lista_vx.append(vx)
            lista_vz.append(vz)

            x = x + vx*t
            z = z + vz*t
            
                        
            v = math.sqrt(math.pow(vx,2) + math.pow(vz,2))
            
            d = math.sqrt(math.pow(x,2) + math.pow(z,2))
            
            
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

