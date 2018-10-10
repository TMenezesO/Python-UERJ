def meuverso(palavras):
    #print(palavras,"x",palavras)
    #print(palavras)
    print(palavras)
    
def minhacancao(verso1, verso2):
    meuverso(verso1)
    meuverso(verso2)
    

list_1=["a","b","c"]
list_2=["d","e","f"]

dict_D={"RB","WR","TE"}
dict_O={"LB","CB","SS"}

for v1 in dict_D:
   for v2 in dict_O:
      minhacancao(v1,v2)
