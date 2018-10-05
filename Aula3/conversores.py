import math

def milhas_para_metros(d_milhas):
   d_metros = d_milhas*1609
   print (d_metros)
   return d_metros

def milhas_para_kms(d_milhas):
   d_km = d_milhas*1.609
   print (d_km)
   return d_km

def metros_para_milhas(d_metros):
   d_milhas = d_metros/1609
   print (d_milhas)
   return d_milhas

def horas_para_segs(t_horas):
   t_segs=t_horas*3600
   print(t_segs)
   return t_segs

def segs_para_horas(t_segs):
   t_horas=(t_segs/3600)
   print(t_horas)
   return t_horas

#milhas_para_metros(100)
#metros_para_milhas(7362)
#horas_para_segs(2)
#segs_para_horas(7200)
