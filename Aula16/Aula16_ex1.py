
class Point:
    """ A classe Ponto representa e manipula as coordenadas x,y . """

    def __init__(self, x=0, y=0):
        """ Cria um novo ponto posicionado na origem. """
        self.x = x
        self.y = y
 
    
class Ponto:
    """ A classe Ponto representa e manipula as coordenadas x,y . """

    def __init__(self, x=0, y=0):
        """ Cria um novo ponto posicionado na origem. """
        self.x = x
        self.y = y
    
    def distancia_da_origem(self):
        """ Calcula minha distânica da origem """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    def reflexao_x(self):
        return (self.x * (-1),self.y)
    
    def distancia_entre_dois_pontos(self,xo,yo):
        """ Calcula a distancia entre dois pontos """
        return ((self.x - xo)**2 + (self.y - yo)**2) ** 0.5
    
    def ponto_medio(p1, p2):
        """ Retorna o ponto médio dos pontos p1 e p2 """
        mx = (p1.x + p2.x)/2
        my = (p1.y + p2.y)/2
        return Ponto(mx, my)
    
    def inclinacao_origem(self):
        return (self.y/self.x)
    
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

print(Ponto(6,8).distancia_entre_dois_pontos(1,1))
print(Ponto(6,8).reflexao_x())
print(Ponto(4,10).inclinacao_origem())


#print(Ponto(3,4).ponto_medio(Ponto(5,12)))

p = Ponto(3, 4)
#print (p.x)
#print (p.y)
#print (p.distancia_da_origem())

q = Ponto (5, 12)
#print (q.x)
#print (q.y)
#print (q.distancia_da_origem())
r = Ponto()
#print(r.x)
#print(r.y)
#print(r.distancia_da_origem())

#p = Point(4, 2)
#q = Point(6, 3)
#r = Point() # origem (0, 0)
#print(p.x, q.y, r.x)





#print(p.x, p.y, q.x, q.y)  # Cada objeto do tipo ponto tem seu próprio x e y