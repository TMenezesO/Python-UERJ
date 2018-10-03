#dict_dt={"d":10,"tmin":43,"tseg":30}
list_tmin=[43]
list_tseg=[30]
list_d=[10]
debug=True

def mph(d_km,t_min,t_s,debug):
    d_m = d_km/1.610 # conversao de km para milhas
    if debug:
        print ("distancia em milhas",d_m)
    th=(t_min/60.0) + (t_s/3600.0) # conversao para o tempo em h
    if debug:
        print ("tempo em horas",th)
    v=d_m/th
    print ("velocidade por milha",v)

mph(10,43,30,debug)
    
#for tmin in list_tmin:
#    for tseg in list_tseg:
#        for d in list_d:
    
#            mph(d,tmin,tseg,debug)


    
    
