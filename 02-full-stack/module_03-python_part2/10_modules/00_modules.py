import sys      # para acceder a las funciones del sistema
sys.path.insert(0, './libraries')   # no funciona desde VSCode, pero sí desde cmd

#import helper


#def render():
#    print(helper.greeting("Naia", "Larrea"))        # Hi Naia Larrea


#render()



# IMPORTAR SOLO UNA FUNCIÓN
from math import sqrt

print(sqrt(25))     # 5.0


# podemos hacer lo mismo con los módulos propios:
#from helper import greeting

#print(greeting("Naia", "Larrea"))



# IMPORTAR USANDO UN ALIAS
import math as m
print(m.sqrt(25))       # 5.0