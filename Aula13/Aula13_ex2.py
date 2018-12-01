#Estudo os métodos do módulo os e faça um script que liste todos os arquivos de um dado diretório assim como de seus subdiretórios. Dica: use o método walk

import os

os.walk("/home/thales/Fisica/Intro_Python")
#os.chdir("/home/thales/Fisica/Intro_Python")
#for root, dirs, files in os.walk(".", topdown = False):
#   for name in files:
#      print(os.path.join(root, name))
#   for name in dirs:
#      print(os.path.join(root, name))