from conversores import *
debug=True

def mph(d_km,t_min,t_s,debug):
    d_milhas = d_km/1.610 # conversao de km para milhas
    if debug:
        print ("distancia em milhas",d_milhas)
    th=(t_min/60.0) + (t_s/3600.0) # conversao para o tempo em h
    if debug:
        print ("tempo em horas",th)
    v=d_m/th
    print ("velocidade por milha",v)

mph(10,43,30,debug)
    



    
    
