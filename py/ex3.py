

def custo(precolivro,nlivros,custo1,custoli,desc):
   custototal=nlivros*(precolivro*desc) + custo1 + (custoli*(nlivros-1))
   print (custototal)

custo(24.95,60,3,0.75,0.6)
#custo(30,10,3,0.75,1)
