import math
import turtle
import matplotlib.pyplot as plt

g=9.81

def pend_mola(xo,zo,k,m,lo):
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

        ax = -(k/m)*((math.sqrt(math.pow(x,2) + math.pow(z,2)))-lo)*(x/(math.sqrt(math.pow(x,2) + math.pow(z,2))))
        az = -g -(k/m)*((math.sqrt(math.pow(x,2) + math.pow(z,2)))-lo)*(z/(math.sqrt(math.pow(x,2) + math.pow(z,2))))
        
        # consertar t, deve ser o intervalo de tempo 
        
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
            
        #print(lista_vx)
        #print(lista_vz)

    plt.plot(lista_d,t1)
    plt.xlabel("tempo s")
    plt.ylabel("distancia m")
    plt.show()
    
    plt.plot(lista_v,t1)
    plt.xlabel("tempo s")
    plt.ylabel("velocidade m/s")
    
    plt.plot(lista_a,t1)
    plt.xlabel("tempo s")
    plt.ylabel("aceleracao m/s^2")
    plt.show()
    
    
    
    plt.plot(lista_vx,lista_x)
    plt.xlabel("velocidade m/s")
    plt.ylabel("distancia m")
    plt.show()
    
  
    plt.plot(lista_vz,lista_z)
    plt.xlabel("velocidade m/s")
    plt.ylabel("distancia m")
    

    with open('your_file.txt', 'w') as f:
        for ax in lista_ax:
            for az in lista_az:
                f.write("%s\n" % ax)
                f.write("\t")
                f.write("%s\n" % az)
                
pend_mola(1,1,1,1,1)

