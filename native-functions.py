# ---------------------- #TODO: Importando funções --------------------------------
import math
import os

x = 16
raiz_quadrada = math.sqrt(x)
print(f'Raiz quadrada de {x} é igual à {raiz_quadrada}')

ang = 45
seno = math.sin(ang)
print(f'O sedo de {ang}° é igual à {seno}')

diretorio = os.getcwd()
print(f'Diretorio atual: {diretorio}')

lista = [10, 20, 30, 40, 50]
tamanho = len(lista)
print(f'A lista {lista} tem {tamanho} elementos')

soma = sum(lista)
print(f'A soma dos elementos da lista {lista} é igual à {soma}')


# ---------------------- #TODO: Funções nativas --------------------------------
# abs()         # sorted()         # type()             # help()
# bool()        # range()          # id()               # locals()
# chr()         # enumerate()      # callable()         # globals()
# int()         # zip()            # isinstance()
# float()       # map()            # range()
# str()         # filter()         # any()
# len()         # abs()            # all()
# max()         # input()          # dir()
# min()         # open()           # eval()
# sum()         # print()          # exec()